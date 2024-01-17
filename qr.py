import qrcode
from PIL import Image 

#"Enter the URL of the data you want to create its QR code."
data='www.linkedin.com/in/abdeldjalil-medjadji-b66671262'
img =qrcode.make(data)
img.save('qr.png')
img=Image.open('qr.png')
img.show()