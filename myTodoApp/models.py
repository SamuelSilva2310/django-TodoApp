from django.db import models
from django.utils import timezone
import datetime


class User(models.Model):
    username = models.CharField(max_length=50, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '{}'.format(self.username)
    
class Task(models.Model):
    task_text = models.CharField(max_length=250, null=True)
    task_due_date = models.DateField(default= timezone.now() + datetime.timedelta(days=7), null=True)
    task_creation_date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)#If User is deleted all users task will be deleted

    def __str__(self):
        return '{}'.format(self.task_text)


