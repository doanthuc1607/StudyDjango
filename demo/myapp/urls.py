from django.urls import path
from . import views

urlpatterns = [
    # go to this kind of empty string "", will call views.home function and execute it
    path("", views.home, name="/"),
    path("home", views.home, name="home"),
    path('update_todo/<int:pk>/', views.updateTodo, name="updateTodo"),
    path('delete/<int:pk>/', views.deleteTodo, name="deleteTodo")
]