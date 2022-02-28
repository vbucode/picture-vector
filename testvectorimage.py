import vectorimage
from PIL import Image

tvi = vectorimage.vectorpixels("004t.jpg", "004t-1.jpg")
ovi = vectorimage.vectorpixels("004.jpg", "004-1.jpg")

for i in ovi:
    c = 0
    for j in tvi:
        if i == j:
            c += 1
    if c == len(tvi):
        print("find!")
        print(ovi[i])
