from picturevector import Picvector
from PIL import Image
import json

dict = {}

tvi = Picvector("il1.jpg")
ovi = Picvector("il.jpg")
t = tvi.vectorpixels()
o = ovi.vectorpixels()

tx = tvi.hx()
ty = tvi.hy()
ox = ovi.hx()
oy = ovi.hy()
print(t)
dict["bm"] = t
with open("bitmaps.json", "a") as file:
    json.dump(dict, file)
    print("save!")
