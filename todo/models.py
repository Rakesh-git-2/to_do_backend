from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoItem(models.Model):

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('complete', 'Complete'),
    ]

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    deadline = models.DateTimeField(null=True)
    is_deleted = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='inprogress')

    def __str__(self):
        return self.title