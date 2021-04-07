from django.shortcuts import render,redirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.

####
#LOGIN AND REGISTER
def register_page(request):
    if request.user.is_authenticated:
        return redirect('myTodoApp:home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account was created for " + user)
                return redirect('myTodoApp:login')

        context = {'form' : form}
        return render(request, 'myTodoApp/register.html', context)


def login_page(request):
    if request.user.is_authenticated:
            return redirect('myTodoApp:home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')  
            user = authenticate(request, username=username,password = password)
        
            if user is not None:
                login(request,user)
                return redirect('myTodoApp:home')
            else:
                messages.info(request, "USername or Password is incorrect")
                return redirect('myTodoApp:login')
        return render(request, 'myTodoApp/login.html')

@login_required(login_url= 'myTodoApp:login')
def logoutUser(request):
    logout(request)
    return redirect('myTodoApp:login')

##########################################

##########################################
            #LISTS
########################################## 

@login_required(login_url= 'myTodoApp:login')
def home(request):
    """This function defines the home page, it should load all TodoLists
    """
    return render(request, 'myTodoApp/lists.html')


@login_required(login_url= 'myTodoApp:login')
def new_List(request):
    """Creates a new List, stores and saves inside the user lists database

    """
    list_name = request.POST['list_name']
    list_type = request.POST['list-type']
    t = ToDoList(name=list_name,list_type=list_type)
    t.save()
    request.user.todolist.add(t)
    return redirect("myTodoApp:home")

@login_required(login_url= 'myTodoApp:login')
def delete_List(request, list_id):
    request.user.todolist.get(id=list_id).delete()
    return redirect("myTodoApp:home")



#Enter a Specific List and display all Tasks
@login_required(login_url= 'myTodoApp:login')
def list_task(request, list_id):
    list = ToDoList.objects.get(id=list_id)
    context = {
        'tasks': list.task_set.all(),
        'list_id': list_id,
        'list_name': list.name,
    }
    return render(request, 'myTodoApp/tasks.html', context=context)


##########################################
            #TASKS
########################################## 

@login_required(login_url= 'myTodoApp:login')
def new_task(request,list_id):
    list = ToDoList.objects.get(id=list_id)
    list.task_set.create(task_text=request.POST['task_text'])
    return redirect(reverse('myTodoApp:list_task',args=(list_id,)))

@login_required(login_url= 'myTodoApp:login')
def delete_task(request,list_id,task_id):
    Task.objects.get(id=task_id).delete()
    return redirect(reverse('myTodoApp:list_task',args=(list_id,)))

@login_required(login_url= 'myTodoApp:login')
def complete_task(request,list_id,task_id):
    print("MADE IT--------------")
    Task.objects.filter(id=task_id).update(task_complete = not Task.objects.get(id=task_id).task_complete)
    print(Task.objects.get(id=task_id).task_complete)
    return redirect(reverse('myTodoApp:list_task',args=(list_id,)))
   

