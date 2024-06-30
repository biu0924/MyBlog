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