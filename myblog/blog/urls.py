from django.urls import path
from . import views
# from .views import login_view, register_view, home_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('blog/get-chat-messages/', views.get_chat_messages, name='get_chat_messages'),
    path('blog/send-chat-message/', views.send_chat_message, name='send_chat_message'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    
在浏览器中查看 "/polls/34/"。
它将运行 detail() 函数并显示您在 URL 中提供的任何 ID。
也可以尝试 "/polls/34/results/" 和 "/polls/34/vote/"，这些将显示占位的结果和投票页面。

当有人请求你网站的页面，
    比如说，"/polls/34/"，Django 会加载 mysite.urls Python 模块，因为它被 ROOT_URLCONF 设置指向。
    它会找到名为 urlpatterns 的变量并按顺序遍历这些模式。
    在找到匹配项 'polls/' 之后，它会剥离匹配的文本（"polls/"），
    然后将剩余的文本 -- "34/" -- 发送给 'polls.urls' URL 配置以进行进一步处理。
    在那里，它会匹配 '<int:question_id>/'，从而调用 detail() 视图，如下所示：
        detail(request=<HttpRequest object>, question_id=34)
    问题 question_id=34 来自 <int:question_id>。
    使用尖括号 "获得" 网址部分后发送给视图函数作为一个关键字参数。
    字符串的 question_id 部分定义了 要使用的名字 ，用来识别相匹配的模式，而 int 部分是一种转换形式，
    用来确定应该匹配网址路径的什么模式。冒号 (:) 用来分隔转换形式和模式名。
'''