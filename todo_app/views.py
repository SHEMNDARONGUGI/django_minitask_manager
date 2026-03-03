from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Create your views here.
def index(request):
    if request.method == 'POST':
        task_data = Task(
        task_name = request.POST['task_name'],
        description = request.POST['description']
    )
        task_data.save()
        return redirect('tasks')

    else: 
        return render(request, 'index.html')
    
def tasks_page(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })

def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method =='POST':
        task.task_name = request.POST['task_name']
        task.description = request.POST['description']
        task.save()
        return redirect('tasks')
    return render(request, 'update_task.html', {'task': task})
    
def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('tasks')
    
    
        


