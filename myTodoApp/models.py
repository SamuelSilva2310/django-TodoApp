from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

import datetime


class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todolist',null=True)#If User is deleted all users task will be deleted
    name = models.CharField(max_length=200, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '{}'.format(self.name)
    
class Task(models.Model):
    
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE ,null=True)#If User is deleted all users task will be deleted
    task_text = models.CharField(max_length=250, null=True)
    task_complete = models.BooleanField(default=False, null=True)

    #task_due_date = models.DateField(default= timezone.now() + datetime.timedelta(days=7), null=True)
    task_creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.task_text)


