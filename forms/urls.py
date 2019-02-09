from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_blog, name='add_blog'),
]
