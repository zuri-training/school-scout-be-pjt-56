from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ScholarshipSerializer

from core.models import Scholarship

# Create your views here.


class ScholarshipListAPIView(ListAPIView):
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer

class ScholarshipDetailAPIView(RetrieveAPIView):
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer