from django.shortcuts import render
import pyqrcode
from django.contrib import messages
from home.default_messages import *

def generated_qrcode(request, url):
    code = pyqrcode.create(url)
    code.svg("static/image/image.svg", scale = 8)
    messages.success(request, DEFAULT_MESSAGES["QRCODE_ADD"])

def index(request):
    if request.method == "POST":
        link = request.POST.get("link", "https://github.com/LucasSantus/")
        generated_qrcode(request, link)

    return render(request, "home/index.html")
