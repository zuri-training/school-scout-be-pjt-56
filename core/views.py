from django.contrib import auth
from django.shortcuts import render
from .models import Testimonial, Review, School
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView
from .serializers import TestimonialSerializer, ReviewSerializer

# Create your views here.

class TestimonialListAPIView(ListAPIView):
    serializer_class = TestimonialSerializer
    queryset = Testimonial.objects.all()
    permission_classes = [permissions.AllowAny]


class ReviewAPIListView(ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Review.objects.filter(school_id=self.kwargs.get('pk'))
        return queryset

    def perform_create(self, serializer):
        author = self.request.user
        school_id = self.kwargs.get('pk')
        school = School.objects.get(pk=school_id)
        serializer.save(author=author, school=school)
from django.shortcuts import render

# Create your views here.
