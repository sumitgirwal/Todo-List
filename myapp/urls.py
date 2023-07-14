from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
]

htmxpatterns = [
    path('create-task/', views.create_task, name="create_task"),
    path('delete-task/<int:pk>/', views.delete_task, name="delete_task"),
    path('list-task/', views.list_task, name="list_task"),
    path('pending-task/', views.pending_task, name="pending_task"),
    path('completed-task/', views.completed_task, name="completed_task"),
    path('mark-completed/<int:pk>/', views.mark_completed, name="mark_completed"),
    path('mark-uncompleted/<int:pk>/', views.mark_uncompleted, name="mark_uncompleted"),
]

urlpatterns += htmxpatterns

