from django.urls import path
from django.contrib.auth import views as auth_views
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.Feed.as_view(), name='feed'),
    path('post_photo/', views.PostPhotoView.as_view(), name='post_photo'),
    path(
        'edit_photo/<int:id>',
        views.EditPhotoView.as_view(),
        name='edit_photo'),
    path('comment/<int:id>', views.CommentView.as_view(), name='comment'),
    path("signup/", views.SignUp.as_view(), name='signup'),
    path(
        'login/',
        auth_views.login, {'template_name': 'app/login.html'},
        name='login'),
    path('logout/', views.LogOut.as_view(), name='logout')
]
