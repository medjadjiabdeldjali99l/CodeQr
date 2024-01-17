import qrcode
from PIL import Image 

#"Enter the URL of the data you want to create its QR code."
data='https://l.facebook.com/l.php?u=https%3A%2F%2Finstagram.com%2Faminestore09%3Figshid%3DMzMyNGUyNmU2YQ%253D%253D%26fbclid%3DIwAR33WjcDRJs9VCzwUQS9e2kQQ0jaPZwYnk8if7vO60YevJxJFxuGwYCXfW8&h=AT17MxgcUfrkXJiNHpdPLoT-d3J1g0--6sjN4LbaUROkqtojlLuohVnO-yGuiUcENJ7dmcO-fuATWOPQrEpCaTKPBO18MKALfz5ZvjDuY5279tB9eRjuJXERMArIY7vgRBUlnQ'
img =qrcode.make(data)
img.save('qr.png')
img=Image.open('qr.png')
img.show()