'''为应用程序users定义URL模式'''
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
app_name = 'users'
urlpatterns = [
    # 登录界面
    path('login/',LoginView.as_view(template_name='users/login.html'),name='login'),
    # 注销
    path('logout/',views.logout_view,name='logout'),
    # 注册页面
    path('register/',views.register,name='register'),
]