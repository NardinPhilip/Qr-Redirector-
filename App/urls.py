# App/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('qr/<slug:slug>/', views.qr_redirect, name='qr_redirect'),
    path('manage-qr/', views.manage_qr, name='manage_qr'),
    path('download-qr/', views.download_qr, name='download_qr'),
]