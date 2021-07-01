from django.urls import path

from .views import (
    ArticleListAPIView, 
    ArticleDetailAPIView, 
    ArticleCreateAPIView, 
    ArticleDestroyAPIView, 
    ArticleUpdateAPIView
    )

app_name = 'articles'

urlpatterns = [
    path('', ArticleListAPIView.as_view(), name='list'),
    path('<slug:slug>', ArticleDetailAPIView.as_view(), name='detail'),
    path('new/', ArticleCreateAPIView.as_view(), name='create'),
    path('<slug:slug>/edit/', ArticleUpdateAPIView.as_view(), name='update'),
    path('<slug:slug>/delete/', ArticleDestroyAPIView.as_view(), name='delete'),
]