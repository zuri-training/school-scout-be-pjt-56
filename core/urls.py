from django.urls import path
from school import views as schoolapi

urlpatterns = [
    #School Related URLS
    path('create-school/', schoolapi.CreateSchoolViews.as_view(), name='create-school'),
    path('get-school-list/', schoolapi.GetSchoolListViews.as_view(), name='get-school-list'),
    path('update-school/<int:pk>/', schoolapi.UpdateSchoolViews.as_view(), name='update-school'),
    path('delete-school/<int:pk>/', schoolapi.DeleteSchoolViews.as_view(), name='delete-school'),
    path('view-school/<int:pk>/', schoolapi.ViewSchoolViews.as_view(), name='view-school'),
]