from django.urls import path

from .views import (
    ScholarshipListAPIView, 
    ScholarshipDetailAPIView, 
    ScholarshipCreateAPIView, 
    ScholarshipUpdateAPIView, 
    ScholarshipDestroyAPIView
    )

app_name = 'scholarships'


urlpatterns = [
    path('', ScholarshipListAPIView.as_view(), name='list'),
    path('<slug:slug>', ScholarshipDetailAPIView.as_view(), name='detail'),
    path('new/', ScholarshipCreateAPIView.as_view(), name='create'),
    path('<slug:slug>/edit/', ScholarshipUpdateAPIView.as_view(), name='update'),
    path('<slug:slug>/delete/', ScholarshipDestroyAPIView.as_view(), name='delete'),
]