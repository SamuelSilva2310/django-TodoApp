# Generated by Django 3.1.7 on 2021-03-30 14:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myTodoApp', '0002_auto_20210330_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 30, 14, 10, 55, 202755, tzinfo=utc)),
        ),
    ]