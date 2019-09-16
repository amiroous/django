from django.urls import path
from project.app_2 import views

urlpatterns = [
    path('', views.index, name='app_2_index'),
]
