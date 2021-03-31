from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Task(models.Model):
    task_text = models.CharField(max_length=250)
    task_due_date = models.DateField(default= timezone.now() + datetime.timedelta(days=7))
    task_creation_date = models.DateTimeField()

    def __str__(self):
        return '{}  {}'.format(self.task_text,self.task_creation_date)
