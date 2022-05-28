from picturevector import Picvector
from PIL import Image
import json

dict = {}

tvi = Picvector("1.jpg")
t = tvi.vectorpixels()

dict["0"] = t
with open("1.json", "a") as file:
    json.dump(dict, file)
    print("save!")
