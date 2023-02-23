from django.urls import path
from core import views

urlpatterns = [
    path('', views.index),
    path('watch/<pk>/', views.videoDetail, name="video-detail"),
]