from django.shortcuts import render,redirect
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
#HOME PAGE
    
@login_required(login_url= 'myTodoApp:login')
def home(request):
    """This function defines the home page, it should load all tasks
    """
    tasks = Task.objects.all().order_by('-task_creation_date')
    front_end_stuff = {
        'tasks' : tasks,
    }
    return render(request, 'myTodoApp/index.html',front_end_stuff)

@login_required(login_url= 'myTodoApp:login')
def new_task(request):
    task = request.POST['task']
    Task.objects.create(task_text=task, task_creation_date=timezone.now())
    return redirect("myTodoApp:home")

@login_required(login_url= 'myTodoApp:login')
def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect("myTodoApp:home")


@login_required(login_url= 'myTodoApp:login')
def user_task(request):
    tasks = Task.objects.filter(user="1")
    front_end_stuff = {
        'tasks' : tasks,
    }
    return render(request, 'myTodoApp/index.html',front_end_stuff)