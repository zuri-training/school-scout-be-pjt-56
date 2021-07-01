from django.urls import path

from .views import (
    CommentListAPIView, 
    CommentDetailAPIView, 
    CommentCreateAPIView, 
    CommentUpdateAPIView, 
    CommentDestroyAPIView
    )

app_name = 'comments'

urlpatterns = [
    path('', CommentListAPIView.as_view(), name='comment_list'),
    path('<pk>', CommentDetailAPIView.as_view(), name='comment_detail'),
    path('new/', CommentCreateAPIView.as_view(), name='create'),
    path('<pk>/edit/', CommentUpdateAPIView.as_view(), name='update'),
    path('<pk>/delete/', CommentDestroyAPIView.as_view(), name='delete'),
]