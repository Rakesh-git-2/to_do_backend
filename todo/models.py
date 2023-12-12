from django.db import models

# Create your models here.
class ToDoItem(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    deadline = models.DateField()