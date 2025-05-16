from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import FileResponse
from django.contrib.auth.models import User
from .models import SharedFile
from .forms import UserRegistrationForm, FileUploadForm, FileShareForm
from django.db import models

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'core/register.html', {'form': form})

@login_required
def home(request):
    # Get files that are either uploaded by the user, shared with them, or public
    files = SharedFile.objects.filter(
        models.Q(uploader=request.user) |
        models.Q(shared_with=request.user) |
        models.Q(is_public=True)
    ).distinct()
    return render(request, 'core/home.html', {'files': files})

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.uploader = request.user
            file.save()
            messages.success(request, 'File uploaded successfully!')
            return redirect('home')
    else:
        form = FileUploadForm()
    return render(request, 'core/upload.html', {'form': form})

@login_required
def download_file(request, file_id):
    file = get_object_or_404(SharedFile, id=file_id)
    if file.uploader == request.user or request.user in file.shared_with.all() or file.is_public:
        return FileResponse(file.file, as_attachment=True)
    messages.error(request, 'You do not have permission to download this file.')
    return redirect('home')

@login_required
def share_file(request, file_id):
    file = get_object_or_404(SharedFile, id=file_id, uploader=request.user)
    if request.method == 'POST':
        form = FileShareForm(request.POST, instance=file)
        if form.is_valid():
            form.save()
            messages.success(request, 'File sharing settings updated!')
            return redirect('home')
    else:
        form = FileShareForm(instance=file)
    return render(request, 'core/share.html', {'form': form, 'file': file})

@login_required
def delete_file(request, file_id):
    file = get_object_or_404(SharedFile, id=file_id, uploader=request.user)
    if request.method == 'POST':
        file.delete()
        messages.success(request, 'File deleted successfully!')
        return redirect('home')
    return render(request, 'core/delete.html', {'file': file})
