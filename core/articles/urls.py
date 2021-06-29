from django.conf import settings
from django.urls import path
from django.contrib import admin

from .views import ArticleListAPIView, ArticleDetailAPIView


urlpatterns = [
    path('', ArticleListAPIView.as_view(), name='article_list'),
    path('<pk>', ArticleDetailAPIView.as_view(), name='article_detail'),

]