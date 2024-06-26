from django.urls import path
from . import views
# from .views import login_view, register_view, home_view

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]