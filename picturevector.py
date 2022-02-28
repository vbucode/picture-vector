#module to work with pixels
from PIL import Image

class Picvector():
    klist = []
    x = 0
    y = 0
    def __init__(self, img):
        self.img = img
        Picvector.x = self.x
        Picvector.y = self.y
    def vectorpixels(self):
        self.im = Image.open(self.img) #открываем изображение с диска
        self.pixels = self.im.load() # список с пикселями
        self.x, self.y = self.im.size # ширина (x) и высота (y) изображения
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = self.pixels[i, j]
                self.klist.append(self.pixels[i,j])
                self.pixels[i, j] = r, g, b
        return self.klist
    def hx():
        return Picvector.x
    def hy():
        return Picvector.y
        
        
