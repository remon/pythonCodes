#example 1
#added by @sagarbabalsure 
#This example create the "QR CODE" for entered string and make the file 'myqr.svg' in your present folder.
#By scanning this qrcode you can go to that url  




import pyqrcode
from pyqrcode import QRCode
s=raw_input("Enter any url to make qr code: ")
url=pyqrcode.create(s)
url.svg("myqr.svg",scale=8)
