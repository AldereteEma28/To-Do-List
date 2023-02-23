import json
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def list_task(request):
    tasks = Task.objects.all()
    return render(request, 'task/list.html',{'tasks':tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task:list_tasks')
    else:
        form = TaskForm()
    return render(request, 'task/add.html', {'form':form})

def delete_task(request,id):
    Task.objects.get(id=id).delete()
    return redirect('task:list_tasks')

def edit_task(request,id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task:list_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/edit.html', {'form':form})

def mark_complete(request,id):
    task = Task.objects.get(id=id)
    if request.method == 'PUT':
        data = json.loads(request.body)
        task.task_completed = data['task_completed']
        task.save()
    return redirect('task:list_tasks')