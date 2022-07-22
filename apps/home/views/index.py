from django.shortcuts import render
import pyqrcode
from django.contrib import messages


def generated_qrcode(request, url):
    code = pyqrcode.create(url)
    code.svg("static/images/image.svg", scale = 7)

def index(request):
    base_url = "https://github.com/LucasSantus/"
    if request.method == "POST":
        link = request.POST.get("link", base_url)
        generated_qrcode(request, link)
    else:
        generated_qrcode(request, base_url)

    return render(request, "home/index.html")
    