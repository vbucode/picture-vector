#module to work with pixels
from PIL import Image

class Picvector():
    klist = []
    slist = []
    def __init__(self, img):
        self.img = img
    def vectorpixels(self):
        global x
        global y
        self.im = Image.open(self.img) #открываем изображение с диска
        self.pixels = self.im.load() # список с пикселями
        self.x, self.y = self.im.size # ширина (x) и высота (y) изображения
        for i in range(self.x):
            self.slist.clear()
            for j in range(self.y):
                r, g, b = self.pixels[i, j]
                self.pixels[i, j] = 255 - r, 255 - g, 255 - b
                self.slist.append(self.pixels[i, j])
            self.klist.append(self.slist)
        self.im.save(self.img + "-1" + ".jpg")
        return self.klist
    def hx(self):
        global x
        x = self.x
        return self.x
    def hy(self):
        global y
        y = self.y
        return self.y
