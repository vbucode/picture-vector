from picturevector import Picvector
from PIL import Image
import json

dict = {}

tvi = Picvector("image0.jpeg")
t = tvi.vectorpixels()

dict["0"] = t

with open("bitmaps.json", "a") as file:
    json.dump(dict, file)
    print("save!")
