from django.urls import path
from project import views as project
from project.app_1 import views as app_1
from project.app_2 import views as app_2

urlpatterns = [
    path('', project.index, name='project_index'),
    path('app/1/', app_1.index, name='ap1_index'),
    path('app/2/', app_2.index, name='ap2_index'),
]