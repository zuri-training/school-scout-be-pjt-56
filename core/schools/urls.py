# from django.urls import path
# from . import views


# urlpatterns = [
#      #School Related URLS
#     path('create-school/', views.CreateSchoolViews.as_view(), name='create-school'),
#     path('get-school-list/', views.GetSchoolListViews.as_view(), name='get-school-list'),
#     path('update-school/<int:pk>/', views.UpdateSchoolViews.as_view(), name='update-school'),
#     path('delete-school/<int:pk>/', views.DeleteSchoolViews.as_view(), name='delete-school'),
#     path('view-school/<int:pk>/', views.ViewSchoolViews.as_view(), name='view-school'),

# ]

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core.schools import views

app_name = 'schools'

urlpatterns = [
    path('', views.SchoolList.as_view(), name='list'),
    path('<slug:slug>/', views.SchoolDetail.as_view(), name='detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)