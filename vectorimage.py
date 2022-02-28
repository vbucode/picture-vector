#module to work with pixels
from PIL import Image

def vectorpixels(img, img2 = 0):
    klist = []
    im = Image.open(img) #открываем изображение с диска
    pixels = im.load() # список с пикселями
    x, y = im.size # ширина (x) и высота (y) изображения
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            klist.append(pixels[i,j])
    return klist
