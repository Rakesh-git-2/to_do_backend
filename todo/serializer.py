from rest_framework import serializers
from .models import ToDoItem
from django.contrib.auth.models import User

class ToDoItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ['id', 'title', 'description', 'deadline',  'user', 'status']
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']