'''
来介绍一下迁移 - 举个例子
Django 的迁移代码是由你的模型文件自动生成的，它本质上是个历史记录，
Django 可以用它来进行数据库的滚动更新，通过这种方式使其能够和当前的模型匹配。
'''
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content[:50]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.jpg')

    def __str__(self):
        return self.user.username