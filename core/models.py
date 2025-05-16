from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class SharedFile(models.Model):
    file = models.FileField(upload_to='shared_files/')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_files')
    upload_date = models.DateTimeField(default=timezone.now)
    is_public = models.BooleanField(default=False)
    shared_with = models.ManyToManyField(User, related_name='shared_files', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-upload_date']
