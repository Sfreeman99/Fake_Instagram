from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('feed/', views.Feed.as_view(), name='feed'),
]
