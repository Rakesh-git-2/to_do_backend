from django.urls import path
from .views import signup, login_view, logout_view, add_todo, get_todos, user_view, update_todo, delete_todo, clear_completed

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('addTodo/', add_todo,name = 'addTodo' ),
    path('getTodos/', get_todos , name = "getTodos" ),
    path('getUser/', user_view, name = 'userview'),
    path('updateTodo/', update_todo, name = "updateTodo"),
    path('<int:pk>/deleteTodo/',delete_todo,name= "deleteTodo"),
    path('clearCompleted/',clear_completed,name = "clearCompleted")
]    