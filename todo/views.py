from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404

from todo.models import Todo


def homepage(request : HttpRequest ) -> HttpResponse:
    # return HttpResponse("Hello World!")
    return render(request, 'home.html')


def todos_page(req : HttpRequest):
    todos = Todo.objects.all().filter(user=req.user)
    return render(req, 'todos.html', {'todos': todos})

def todo_page(req : HttpRequest, id : str):
    todo = get_object_or_404(Todo, id=id)
    return render(req, 'todo.html', {'todo': todo})