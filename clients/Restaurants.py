from datetime import date
import qrcode
import requests as re

from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

class Restaurant :
    def __init__(self, names, website):
        self.names= names
        self.website = website

    #def __generateQrCode__(self, n,link, feature):
    def generateQrCode(self, n, link,logo = 'No logo', feature="MENU"):
        now = date.today().strftime("%Y-%m-%d")

        ## a debugger
        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
        feature = feature.upper()
        if logo=='No logo':
            img = qrcode.make(link)
            nameSave = f"{n}__{feature}__{now}.png".replace(" ","_")

        else:
            img = qr.make_image(embeded_image_path=logo)
            nameSave = f"{n}__{feature}__{now}__WithLogo.png".replace(" ","_")


        print(nameSave)
        img.save(f"QrCodemenuRestaurant/{nameSave}")
        ## fonction d'envoie de l'image au clients par email ou whatsapp


rest = Restaurant(names="Africa Data Entry", website="africadataentry.com")

rest.generateQrCode(n=rest.names,link='https://africadataentry.com/wp-content/uploads/2024/10/WhatsApp-Image-2024-10-14-at-11.00.31-AM.jpeg',logo="Logo .Africa data entry 04ai.jpg")
#print("end