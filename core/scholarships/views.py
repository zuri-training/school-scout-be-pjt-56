from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView, 
    CreateAPIView, 
    UpdateAPIView, 
    DestroyAPIView
)

from .serializers import ScholarshipSerializer
from core.models import Scholarship


class ScholarshipListAPIView(ListAPIView):
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer


class ScholarshipDetailAPIView(RetrieveAPIView):
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'


class ScholarshipCreateAPIView(CreateAPIView):
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer


class ScholarshipUpdateAPIView(UpdateAPIView):
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer
    lookup_url_kwarg = 'slug'


class ScholarshipDestroyAPIView(DestroyAPIView):
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer
    lookup_url_kwarg = 'slug'
