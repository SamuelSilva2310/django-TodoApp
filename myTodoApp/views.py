from django.shortcuts import render,redirect
from django.utils import timezone

from .models import Task
# Create your views here.

#HOME PAGE
    
def home(request):
    """This function defines the home page, it should load all tasks
    """
    tasks = Task.objects.all().order_by('-task_creation_date')
    front_end_stuff = {
        'tasks' : tasks,
    }
    return render(request, 'myTodoApp/index.html',front_end_stuff)


def new_task(request):
    task = request.POST['task']
    Task.objects.create(task_text=task, task_creation_date=timezone.now())
    return redirect("/")

def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect("/")