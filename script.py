import pyqrcode

url = pyqrcode.create ('https://oondev.github.io/')
url.svg ('oondev.svg', scale = 8)
url.eps ('oondev.eps', scale = 2)
print (url.terminal (quiet_zone = 1))