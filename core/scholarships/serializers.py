from rest_framework import serializers

from .models import Scholarship


class ScholarshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scholarship
        fields = [
            'pk',
            'name',
            'slug',
            'image',
            'description',
            'snippets',
            'requirements',
            'school',
            'website',
            'whatsapp',
            'instagram',
            'facebook',
            'twitter',
            'date',
        ]
        extra_kwargs = {
            'image': {'required': False}
        }

