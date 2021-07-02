from rest_framework import serializers
from .models import Testimonial, UniversityReview


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'


class UniversityReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityReview
        #fields = ['id', 'review', 'rating']
        fields = '__all__'

