from django.shortcuts import render
from .models import ToDoItem

# Create your views here.

def to_do_items(request):
    todos = ToDoItem.objects.all()
    context = {'todo_items':todos}
    return render(request,"todo/to_do_list.html",context)

