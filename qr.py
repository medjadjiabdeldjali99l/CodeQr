import qrcode
from PIL import Image 

#"Enter the URL of the data you want to create its QR code."
data='https://www.tiktok.com/@djadjooooooo?is_from_webapp=1&sender_device=pc'
img =qrcode.make(data)
img.save('qr.png')
img=Image.open('qr.png')
img.show()