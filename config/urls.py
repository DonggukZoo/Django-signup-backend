from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', include('accounts.urls')),  # ✅ 여기 꼭 있어야 함!
]