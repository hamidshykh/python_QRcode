import qrcode 
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size = 10 , border = 4)
qr.add_data("https://www.google.com/")
qr.make(fit = True)
img = qr.make_image(fill_color=(255, 0, 0), back_color=(0, 0, 255))
img.save("google_qrcode.png")