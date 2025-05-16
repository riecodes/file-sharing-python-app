from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import SharedFile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = SharedFile
        fields = ['title', 'description', 'file', 'is_public']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class FileShareForm(forms.ModelForm):
    class Meta:
        model = SharedFile
        fields = ['shared_with']
        widgets = {
            'shared_with': forms.CheckboxSelectMultiple(),
        } 