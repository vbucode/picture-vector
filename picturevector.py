#module to work with pixels
from PIL import Image

class Picvector():
    klist = []
    def __init__(self, img):
        self.img = img
    def vectorpixels(self):
        global x
        global y
        self.im = Image.open(self.img) #открываем изображение с диска
        self.pixels = self.im.load() # список с пикселями
        self.x, self.y = self.im.size # ширина (x) и высота (y) изображения
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = self.pixels[i, j]
                self.klist.append(self.pixels[i,j])
                self.pixels[i, j] = r, g, b
        return self.klist
    def hx(self):
        global x
        x = self.x
        return self.x
    def hy(self):
        global y
        y = self.y
        return self.y
        
        
