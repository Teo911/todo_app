from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.ahoj),
    path('addTodo/', views.addTodo),
    path('deleteTodo/<int:todo_id>', views.deleteTodo)
]
