from django.shortcuts import render, get_object_or_404
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all().values_list('id', 'title')
    data = [{'id': todo[0], 'title': todo[1]} for todo in todos]
    return render(request, 'todo_list.html', {'data': data})

def todo_info(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    info = {
        'title': todo.title,
        'description': todo.description,
        'start_date': todo.start_date,
        'end_date': todo.end_date,
        'is_completed': todo.is_completed,
    }
    return render(request, 'todo_info.html', {'data': info})

