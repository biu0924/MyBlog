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
            'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M')
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




'''
    Django 中的视图的概念是「一类具有相同功能和模板的网页的集合」。
    比如，在一个博客应用中，你可能会创建如下几个视图：
    博客首页——展示最近的几项内容。
    内容“详情”页——详细展示某项内容。
    以年为单位的归档页——展示选中的年份里各个月份创建的内容。
    以月为单位的归档页——展示选中的月份里各天创建的内容。
    以天为单位的归档页——展示选中天里创建的所有内容。
    评论处理器——用于响应为一项内容添加评论的操作。
'''
'''
    在 Django 中，网页和其他内容都是从视图派生而来。
    每一个视图表现为一个 Python 函数（或者说方法，如果是在基于类的视图里的话）。
    Django 将会根据用户请求的 URL 来选择使用哪个视图（更准确的说，是根据 URL 中域名之后的部分）。
'''