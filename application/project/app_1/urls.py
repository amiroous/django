from django.urls import path
from project.app_1 import views

urlpatterns = [
    path('', views.index, name='app_1_index'),
]
