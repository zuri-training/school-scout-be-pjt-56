from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import CommentSerializer
from core.models import Comment

# Create your views here.


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetailAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer