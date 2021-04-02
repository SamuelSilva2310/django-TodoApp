# Generated by Django 3.1.7 on 2021-04-02 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myTodoApp', '0014_auto_20210402_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_complete',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='todolist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task', to='myTodoApp.todolist'),
        ),
    ]