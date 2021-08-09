from django.db import models
import pyqrcode

class Generated(models.Model):
    url = models.CharField(
        verbose_name = "URL",
        max_length = 255,
    )
    
    image = models.ImageField(
        verbose_name = "Image",
    )  

    class Meta:
        verbose_name = "Generated"
        verbose_name_plural = "Generated's"
        
    def generated_qrcode(self):
        code = pyqrcode.create(self.url)
        code.svg ('oondev.svg', scale = 8)
        code.eps ('oondev.eps', scale = 2)
        print (code.terminal (quiet_zone = 1))

    def __str__(self):
        return self.url