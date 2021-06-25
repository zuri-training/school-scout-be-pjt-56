from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from .views import UserViewSet


GET_OPTIONS = {'get': 'list'}

RETRIEVE_OPTIONS = {'get': 'retrieve'}

POST_OPTIONS = {'post': 'create'}

LIST_OPTIONS = {
    'get': 'list',
    'post': 'create'
}

DETAIL_OPTIONS = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('/registration/', include('rest_auth.registration.urls')),
    path('/users/', UserViewSet.as_view(GET_OPTIONS), name="users"),
]
