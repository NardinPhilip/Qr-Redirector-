# models.py
from django.db import models

class QRCodeLink(models.Model):
    slug = models.SlugField(unique=True, default='default-qr')
    target_url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"QR Code for {self.target_url}"