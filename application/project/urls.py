from django.urls import path, include
from project import views as project

urlpatterns = [
    path('', project.index, name='project_index'),
    path('app/1/', include('project.app_1.urls')),
    path('app/2/', include('project.app_2.urls')),
]
