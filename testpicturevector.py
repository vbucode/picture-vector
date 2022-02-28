from picturevector import Picvector
from PIL import Image

tvi = Picvector("il1.jpg")
ovi = Picvector("il.jpg")
for i in ovi.vectorpixels():
    c = 0
    for j in tvi.vectorpixels():
        if i == j:
            c += 1
    if c == (Picvector.hx() * Picvector.hy()):
        print("find!")
