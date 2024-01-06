from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addTodo),
    path('update/<int:pk>/', views.updateTodo),
    path('delete/<int:pk>/', views.deleteTodo)
]