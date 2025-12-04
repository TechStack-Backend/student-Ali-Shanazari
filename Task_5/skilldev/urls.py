from django.urls import path
from . import views
from .api_views import developer_api

urlpatterns = [
    # Developers
    path('developers/', views.DeveloperListView.as_view(), name='developer_list'),
    path('developers/new/', views.DeveloperCreateView.as_view(), name='developer_create'),
    path('developers/<int:pk>/', views.DeveloperDetailView.as_view(), name='developer_detail'),
    path('developers/<int:pk>/edit/', views.DeveloperUpdateView.as_view(), name='developer_update'),
    path('developers/<int:pk>/delete/', views.DeveloperDeleteView.as_view(), name='developer_delete'),

    # Projects
    path('projects/', views.ProjectListView.as_view(), name='project_list'),
    path('projects/new/', views.ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:pk>/edit/', views.ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),

    #api
    path("api/developers/", developer_api, name="developer_api"),
]