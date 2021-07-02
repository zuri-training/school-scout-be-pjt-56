from django.urls import path
from .views import TestimonialListAPIView, UniversityReviewAPIListView

urlpatterns = [
    path('testimonials/', TestimonialListAPIView.as_view()),
    path('schools/<int:pk>/review/', UniversityReviewAPIListView.as_view()),
]