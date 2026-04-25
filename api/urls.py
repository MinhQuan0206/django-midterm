from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
    path('tasks/', views.task_list_create, name='task_list_create'),
]