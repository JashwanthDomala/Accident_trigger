# detection/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page for video upload
    path('process_video/', views.process_video, name='process_video'),  # Process uploaded video
]
