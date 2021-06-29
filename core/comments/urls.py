from django.conf import settings
from django.urls import path
from django.contrib import admin

from .views import CommentListAPIView, CommentDetailAPIView


urlpatterns = [
    path('', CommentListAPIView.as_view(), name='comment_list'),
    path('<pk>', CommentDetailAPIView.as_view(), name='comment_detail'),
]