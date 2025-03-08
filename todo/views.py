from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render, get_object_or_404

from todo.forms import TodoForm
from todo.models import Todo


def homepage(request : HttpRequest ) -> HttpResponse:
    # return HttpResponse("Hello World!")
    return render(request, 'home.html')

def todo_create(req : HttpRequest):
    form = TodoForm()
    if req.method == "POST":
        form = TodoForm(req.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = req.user
            todo.save()
            return redirect("/todo")
    return render(req, 'create_todo.html', {'form': form})

def todos_page(req : HttpRequest):
    todos = Todo.objects.all().filter(user=req.user)
    return render(req, 'todos.html', {'todos': todos})

def todo_page(req : HttpRequest, id : str):
    todo = get_object_or_404(Todo, id=id)
    authorized = todo.user == req.user
    if not authorized:
        todo = None
    return render(req, 'todo.html', {'todo': todo, "authorized": authorized})