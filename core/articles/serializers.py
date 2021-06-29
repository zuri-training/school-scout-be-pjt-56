from rest_framework import serializers
from django.contrib.auth.models import User

from core.models import Article


class ArticleSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Article
        fields = [
            'pk',
            'author',
            'title',
            'body',
            'date',
        ]
        extra_kwargs = {
            'image': {'required': False}
        }

