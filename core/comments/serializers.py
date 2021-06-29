from rest_framework import serializers
from django.contrib.auth.models import User

from core.models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'pk',
            'article',
            'commenter',
            'body',
            'date',
        ]

