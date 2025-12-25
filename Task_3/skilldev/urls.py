from django.urls import path
from . import views

urlpatterns = [
    path('developers/', views.developer_list, name='developer_list'),
    path('projects/', views.project_list, name='project_list'),
    path('developers/new/', views.developer_create, name='developer_create'),
    path('projects/new/', views.project_create, name='project_create'),
]
