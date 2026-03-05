from django.urls import path 
from .views import view_api
urlpatterns = [
    path('',view_api,name='api_view')
]
