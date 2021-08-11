from django.shortcuts import render
from home.models import *

import pyqrcode

def generated_qrcode(link):
    code = pyqrcode.create(link)
    code.svg("static/image/image.svg", scale = 8)

def index(request):
    if request.POST:
        link = request.POST.get("link", None)
        
    generated_qrcode(link)

    return render(request, "home/index.html")
