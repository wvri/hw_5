from django.urls import path
from . import views

urlpatterns = [
    path("todos/", views.todo_list, name="todos"),
    path("", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("todos/", views.todo_list, name="todo_list"),
    path("<int:id>/", views.todo_detail, name="todo_detail"),
    path("todos/new/", views.create_todo, name="create_todo"),
    path("todos/<int:todo_id>/delete/", views.delete_todo, name="delete_todo"),
]
