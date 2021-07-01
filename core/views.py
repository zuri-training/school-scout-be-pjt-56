from rest_framework import generics
from .models import StudentAccount
from .serializers import StudentAccountSerializer

class ListStudentAccount(generics.ListAPIView):
    queryset = StudentAccount.objects.all()
    serializer_class = StudentAccountSerializer

class DetailStudentAccount(generics.RetrieveAPIView):
    queryset = StudentAccount.objects.all()
    serializer_class = StudentAccountSerializer
