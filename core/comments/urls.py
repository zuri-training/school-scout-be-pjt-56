from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core.comments import views

app_name = 'comments'

urlpatterns = [
    path('', views.CommentList.as_view(), name='comment_list'),
    path('<pk>/', views.CommentDetail.as_view(), name='comment_detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)