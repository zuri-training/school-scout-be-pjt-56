from rest_framework import serializers
from .models import StudentAccount

class StudentAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAccount
        fields = ('__all__')