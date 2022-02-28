import picturevector
from PIL import Image

tvi = picturevector.vectorpixels("004t.jpg", "004t-1.jpg")
ovi = picturevector.vectorpixels("004.jpg", "004-1.jpg")

for i in ovi:
    c = 0
    for j in tvi:
        if i == j:
            c += 1
    if c == len(tvi):
        print("find!")
        print(ovi[i])
