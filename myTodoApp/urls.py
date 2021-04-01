from django.urls import path

from . import views


app_name = 'myTodoApp'
urlpatterns = [
    path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.home, name='home'),
    path('user_task', views.user_task, name="user_task"),

    path('new_task',views.new_task, name="new_task"), 
    path('delete_task/<int:task_id>',views.delete_task, name="delete_task"),

   
]