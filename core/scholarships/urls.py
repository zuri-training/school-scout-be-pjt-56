from django.conf import settings
from django.urls import path
from django.contrib import admin

from .views import ScholarshipListAPIView, ScholarshipDetailAPIView


urlpatterns = [
    path('', ScholarshipListAPIView.as_view(), name='scholarship_list'),
    path('<pk>', ScholarshipDetailAPIView.as_view(), name='scholarship_detail'),
]