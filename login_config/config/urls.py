from django.contrib import admin
from django.urls import path
from django.http import HttpResponse  # 간단한 뷰 만들기 위해 임포트

def home(request):
    return HttpResponse("Hello, Django!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # 기본 경로로 접속하면 Hello, Django!
]