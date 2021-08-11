from django.db import models

from PIL import Image
import pyqrcode

class Generated(models.Model):
    url = models.CharField(
        verbose_name = "URL",
        max_length = 255,
    )

    image = models.ImageField(upload_to = "image/")

    class Meta:
        verbose_name = "Generated"
        verbose_name_plural = "Generated's"
        
    def generated_qrcode(self):
        code = pyqrcode.create(self.url)
        return code.svg("static/image/image.svg", scale = 8)

    def __str__(self):
        return self.url