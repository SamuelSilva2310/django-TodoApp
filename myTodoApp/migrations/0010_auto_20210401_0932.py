# Generated by Django 3.1.7 on 2021-04-01 08:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myTodoApp', '0009_auto_20210401_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_due_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 8, 8, 32, 52, 516896, tzinfo=utc)),
        ),
    ]