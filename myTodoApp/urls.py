from django.urls import path

from . import views


app_name = 'myTodoApp'
urlpatterns = [
    
    path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    
    path('new_list',views.new_List, name="new_list"), 
    path('delete_list/<int:list_id>',views.delete_List, name="delete_list"),

    path('new_task/<int:list_id>',views.new_task, name="new_task"), 
    path('delete_task/<int:task_id>',views.delete_task, name="delete_task"),
    
    path('', views.home, name='home'),
    path('list/<int:list_id>', views.list_task, name="list_task")
    #path('user_task', views.user_task, name="user_task"),
   
]