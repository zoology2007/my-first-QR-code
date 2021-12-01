import pyqrcode 
from pyqrcode import QRCode
import png
www="en.wikipedia.org"
website=pyqrcode.create(www)

website.png("theqr.png",scale=10)

website.svg("theqr.svg",scale=10)