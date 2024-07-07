from . import views

from django.urls import path, include

urlpatterns = [
    path('download',views.download_video, name='download'),
]