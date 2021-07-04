from django.urls import path
from .views import TestimonialListAPIView, ReviewAPIListView

urlpatterns = [
    path('testimonials/', TestimonialListAPIView.as_view()),
    path('schools/<int:pk>/reviews/', ReviewAPIListView.as_view()),
]