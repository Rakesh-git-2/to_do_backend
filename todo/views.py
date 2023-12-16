from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .models import ToDoItem
from .serializer import ToDoItemsSerializer, UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if not username or not password:
        return JsonResponse({'error': 'Username and password are required.'}, status=400)
    
    if User.objects.filter(email=email).exists():
        return JsonResponse({'error': 'User with same email already exists'}, status=403)
    
    if User.objects.filter(username=username).exists():
        return JsonResponse({'error': 'User with same username already exists. Try a different one'}, status=403)

    user = User.objects.create_user(username=username, password=password, email=email)

    return JsonResponse({'message': 'User created successfully.'}, status=201)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    print(email,password)
    user = User.objects.filter(email=email).first()
    if user:
        user = authenticate(request, username = user.username, password=password)
    
    if user:
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return JsonResponse({'token': token.key, 'message': 'Login successful.'})
    else:
        return JsonResponse({'error': 'Invalid credentials.'}, status=401)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_view(request):
    user = request.user
    result = UserSerializer(user)
    return JsonResponse(result.data,status=200,safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    request.auth.delete()
    return JsonResponse({'message': 'Logout successful.'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_todo(request):
    title = request.data['title']
    description = request.data['description']
    deadline = request.data['deadline']
    user = request.user
    status = 'active'
    todo = ToDoItem(title=title,user=user,status=status,description=description,deadline=deadline)
    todo.save()
    serde = ToDoItemsSerializer(todo)
    return JsonResponse(serde.data,status=201,safe=False)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_todo(request):
    id = request.data["id"]
    user = request.user
    todo = ToDoItem.objects.get(user=user,id=id)
    todo.title = request.data['title']
    todo.description = request.data['description']
    todo.deadline = request.data['deadline']
    todo.status = request.data['status']
    todo.save()
    serde = ToDoItemsSerializer(todo)
    return JsonResponse(serde.data,status=201,safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_todos(request):
    todos = ToDoItem.objects.filter(user=request.user,is_deleted=False).order_by('status','deadline')
    serde = ToDoItemsSerializer(todos,many=True)
    return JsonResponse({'items' : serde.data},status=201,safe=False)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_todo(request,pk):
    todo = ToDoItem.objects.get(user=request.user,id=pk)
    todo.is_deleted = True
    todo.save()
    return JsonResponse({'message':'Item deleted'},status=200)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def clear_completed(request):
    todo = ToDoItem.objects.filter(user=request.user,status='completed')
    if todo.exists():
        todo.update(is_deleted=True)
    return JsonResponse({'message':'Items deleted'},status=200)
