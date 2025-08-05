from django.urls import path
from .views import signup_view

urlpatterns = [
    path('', signup_view, name='signup')  # http://127.0.0.1:8000/signup/ 처리
]