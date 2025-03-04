from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("todo_list")
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, "todo_list.html", {"todos": todos})

@login_required
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    return render(request, "todo_detail.html", {"todo": todo})

@login_required
def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect("todo_list")
    else:
        form = TodoForm()
    return render(request, "todo_form.html", {"form": form})

@login_required
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.delete()
    return redirect("todo_list")
