from django.urls import path
from . import views


app_name = 'myTodoApp'
urlpatterns = [
    path('', views.home, name='index'),
    path('new_task',views.new_task,name="new_task"), 
    path('delete_task/<int:task_id>',views.delete_task,name="delete_task")
]