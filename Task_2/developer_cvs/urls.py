from django.urls import path
from . import views


urlpatterns = [
    path('developers/', views.developers_list_view, name='developers-list'),
    path('developers/<str:username>', views.developers_cv_view, name='developers-cv'),
]