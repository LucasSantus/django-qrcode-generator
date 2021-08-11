from django.shortcuts import render
from django.contrib import messages
from home.models import *

import pyqrcode

def index(request):
    context = None
    if request.POST:
        link = request.POST.get("link", None)

        code = Generated()
        code.url = link
        # print(code.generated_qrcode())
        code.image = "static/image/image.svg"
        code.save()
    
        context = {
            'url': code.image,
        }

    return render(request, "home/index.html", context)
