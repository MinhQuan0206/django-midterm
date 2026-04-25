from django.contrib import admin
from django.urls import path, include # Nhớ import thêm 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), # Chuyển hướng các request bắt đầu bằng /api/ vào app api
]