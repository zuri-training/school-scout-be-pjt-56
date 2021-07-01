from django.urls import path
from .views import ListStudentAccount, DetailStudentAccount

urlpatterns = [
    path('<int:pk>/', DetailStudentAccount.as_view()),
    path('', ListStudentAccount.as_view()),
]
