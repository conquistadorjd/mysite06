from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.

def index(request):
    context = Task.objects.all()
    return render(request, 'todo/index.html',{'context':context})    

def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'todo/detail.html', {'task': task})    

def newtask(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/todo/")
    return render(request, 'todo/newtask.html', {'form':form})

def edit(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    print("**", task.title)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect("/todo/")
    return render(request, 'todo/newtask.html', {'form':form})


def delete(request, task_id):
    # print(request.method )  
    task = Task.objects.get(id=task_id)  
    task.delete()  
    return redirect("/todo/") 
