from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('upload/', views.upload_file, name='upload'),
    path('download/<int:file_id>/', views.download_file, name='download'),
    path('share/<int:file_id>/', views.share_file, name='share'),
    path('delete/<int:file_id>/', views.delete_file, name='delete'),
] 