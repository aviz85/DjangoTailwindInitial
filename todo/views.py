from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Todo
import json


@ensure_csrf_cookie
def todo_list(request):
  todos = Todo.objects.all().order_by('-created_at')
  return render(request, 'todo/todo_list.html', {'todos': todos})


@require_POST
def add_todo(request):
  data = json.loads(request.body)
  todo = Todo.objects.create(title=data['title'])
  return JsonResponse({
      'success': True,
      'todo': {
          'id': todo.id,
          'title': todo.title,
          'completed': todo.completed
      }
  })


@require_POST
def toggle_todo(request, todo_id):
  todo = get_object_or_404(Todo, id=todo_id)
  todo.completed = not todo.completed
  todo.save()
  return JsonResponse({'success': True, 'completed': todo.completed})


@require_POST
def delete_todo(request, todo_id):
  todo = get_object_or_404(Todo, id=todo_id)
  todo.delete()
  return JsonResponse({'success': True})
