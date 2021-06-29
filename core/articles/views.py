from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ArticleSerializer

from core.models import Article

# Create your views here.


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetailAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer