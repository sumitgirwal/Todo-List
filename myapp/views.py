from django.shortcuts import render, HttpResponse
from .models import Task

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


def create_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        print("##############", title)
        task = Task.objects.create(title=title)
        task.save()
        tasks = Task.objects.all()
        return render(request, 'list-task.html', {'tasks': tasks})
    
def delete_task(request, pk):
    if request.method == "DELETE":
        task = Task.objects.get(pk=pk)
        task.delete()
        tasks = Task.objects.all()
        return render(request, 'list-task.html', {'tasks': tasks})


def list_task(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        return render(request, 'list-task.html', {'tasks': tasks})


def pending_task(request):
    if request.method == "GET":
        tasks = Task.objects.filter(completed=False)
        print(tasks)
        return render(request, 'list-task.html', {'tasks': tasks})

def completed_task(request):
    if request.method == "GET":
        tasks = Task.objects.filter(completed=True)
        return render(request, 'list-task.html', {'tasks': tasks})

def mark_completed(request, pk):
    if request.method == "GET":
        task = Task.objects.get(pk=pk)
        task.completed = True
        task.save()
        tasks = Task.objects.all()
        return render(request, 'list-task.html', {'tasks': tasks})

def mark_uncompleted(request, pk):
    if request.method == "GET":
        task = Task.objects.get(pk=pk)
        task.completed = False
        task.save()
        tasks = Task.objects.all()
        return render(request, 'list-task.html', {'tasks': tasks})