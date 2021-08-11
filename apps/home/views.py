from django.shortcuts import render
from home.models import *

import pyqrcode

def generated_qrcode(url):
    code = pyqrcode.create(url)
    code.svg("static/image/image.svg", scale = 8)

def index(request):
    if request.POST:
        link = request.POST.get("link", "https://github.com/LucasSantus/")
        generated_qrcode(link)

    context = {
        'page_title': 'QR Code Generated',
    }

    return render(request, "home/index.html", context)
