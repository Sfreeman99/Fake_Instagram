from django.urls import path
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
]
