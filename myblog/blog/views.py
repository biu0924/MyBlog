from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import ChatMessage


# 首页
def home_view(request):
    return render(request, 'home.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})
        user = User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'register.html')

def get_chat_messages(request):
    messages = ChatMessage.objects.order_by('timestamp')
    messages_data = [
        {
            'user': message.user.username,
            'avatar': message.user.profile.avatar.url,  # 假设用户模型有avatar字段
            'content': message.content,
            'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }
        for message in messages
    ]
    return JsonResponse({'messages': messages_data})

@csrf_exempt
@login_required
def send_chat_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        content = data.get('content', '')
        if content:
            message = ChatMessage(user=request.user, content=content)
            message.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'error': 'Empty content'}, status=400)
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)