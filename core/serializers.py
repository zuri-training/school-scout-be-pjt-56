from rest_framework import serializers
from .models import Testimonial, Review, School


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    school_name = serializers.ReadOnlyField(source='school.name')
    author_name = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Review
        fields = ['id', 'review', 'rating', 'author_name', 'school_name']

class SchoolSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(required=False)
    class Meta:
        model = School
        fields = '__all__'
