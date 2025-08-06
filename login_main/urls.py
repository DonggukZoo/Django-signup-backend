from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # 로그인 뷰 불러오기

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]
