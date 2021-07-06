from django.urls import path
from courses import views as courseapi

urlpatterns = [
    #School Related URLS
    path('create-course/', courseapi.CreateCourseViews.as_view(), name='create-course'),
    path('get-course-list/', courseapi.GetCourseListViews.as_view(), name='get-course-list'),
    path('update-course/<int:pk>/',courseapi.UpdateCourseViews.as_view(), name='update-course'),
    path('delete-course/<int:pk>/', courseapi.DeleteCourseViews.as_view(), name='delete-course'),
    path('view-course/<int:pk>/', courseapi.ViewCourseViews.as_view(), name='view-course'),
]