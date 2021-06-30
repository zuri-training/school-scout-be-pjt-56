from django.urls import path
from courses import views as coursesapi

 # Course Related URLS
urlpatterns = [
    path('create-course/', coursesapi.CreateCourseViews.as_view(), name='create-course'),
    path('get-course-list/', coursesapi.GetCourseListViews.as_view(), name='get-course-list'),
    path('update-course/<int:pk>/', coursesapi.UpdateCourseViews.as_view(), name='update-course'),
    path('delete-course/<int:pk>/', coursesapi.DeleteCourseViews.as_view(), name='delete-course'),
    path('view-course/<int:pk>/', coursesapi.ViewCourseViews.as_view(), name='view-course'),
 ]