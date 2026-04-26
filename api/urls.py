from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
    path('tasks/', views.task_list_create, name='task_list_create'),
    path('notes/', views.note_list_create, name='note_list_create'),
    path('notes/<int:id>/', views.note_detail_api, name='note_detail_api'),
]