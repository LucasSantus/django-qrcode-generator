from django.shortcuts import render
import pyqrcode

def generated_qrcode(url):
    code = pyqrcode.create(url)
    code.svg("static/image/image.svg", scale = 8)

def index(request):
    if request.method == "POST":
        link = request.POST.get("link", "https://github.com/LucasSantus/")
        generated_qrcode(link)

    return render(request, "home/index.html")
