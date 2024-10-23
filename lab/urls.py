from django.urls import path
from . import views

urlpatterns = [
    path('', views.lab, name='lab'),
    path('transform_image/', views.transform_image, name='transform_image')
]