from rest_framework import serializers
from core.models import School
#from course.serializers import CourseSerializer


class SchoolSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = School
        fields = '__all__'