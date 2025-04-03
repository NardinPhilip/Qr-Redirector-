# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('', include('App.urls')),  # Include your app's URLs (assuming your app is named 'qrapp')
]