# Generated by Django 3.1.7 on 2021-03-31 08:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myTodoApp', '0005_auto_20210330_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 31, 8, 36, 0, 153128, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_due_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 7, 8, 36, 0, 153128, tzinfo=utc)),
        ),
    ]
