from picturevector import Picvector
from PIL import Image
import json

dict = {}

tvi = Picvector("p.jpg")
t = tvi.vectorpixels()

tx = tvi.hx()
ty = tvi.hy()
print(t)
dict["bm"] = t
with open("bitmaps.json", "a") as file:
    json.dump(dict, file)
    print("save!")
