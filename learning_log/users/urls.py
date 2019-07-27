"""为应用程序users定一URL模式"""

from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    # 登陆页面
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    # 注销
    url(r'^logout/$', views.logout_view, name='logout'),
    # 注册
    url(r'^register/$', views.register, name='register'),
]

app_name = 'users'
