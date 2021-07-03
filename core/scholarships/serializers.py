from rest_framework import serializers

from core.models import Scholarship


class ScholarshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scholarship
        fields = [
            'pk',
            'name',
            'slug',
            'donor',
            'image',
            'description',
            'institution',
            'course_name',
            'funding',
            'degree_level',
            'amount',
            'deadline',
            'requirements',
            'date_published',
            'contact',
            'telephone',
            'email',
            'website',
        ]
        extra_kwargs = {
            'image': {'required': False}
        }


