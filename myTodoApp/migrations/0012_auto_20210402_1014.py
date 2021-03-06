# Generated by Django 3.1.7 on 2021-04-02 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myTodoApp', '0011_auto_20210401_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='task_due_date',
        ),
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
        migrations.AddField(
            model_name='task',
            name='task_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='task',
            name='todolist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myTodoApp.todolist'),
        ),
    ]
