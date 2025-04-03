# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import qrcode
from io import BytesIO
from .models import QRCodeLink
from django.conf import settings
import os

def qr_redirect(request, slug):
    qr_link = get_object_or_404(QRCodeLink, slug=slug)
    print(f"Redirecting to: {qr_link.target_url}")
    return redirect(qr_link.target_url)
    
def manage_qr(request):
    qr_link, created = QRCodeLink.objects.get_or_create(slug='default-qr')
    
    if request.method == 'POST':
        new_url = request.POST.get('target_url')
        if new_url:
            qr_link.target_url = new_url
            qr_link.save()
            return redirect('manage_qr')
    
    return render(request, 'App/qr_code_manager.html', {'qr_link': qr_link})

def download_qr(request):
    # Generate QR code pointing to the redirect URL
    qr_link = get_object_or_404(QRCodeLink, slug='default-qr')
    qr_url = request.build_absolute_uri(f"/qr/{qr_link.slug}/")
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_url)
    qr.make(fit=True)
    
    # Create image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save to buffer
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    
    # Return as downloadable file
    response = HttpResponse(buffer, content_type='image/png')
    response['Content-Disposition'] = 'attachment; filename="qr_code.png"'
    return response