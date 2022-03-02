#module to work with pixels
from PIL import Image

class Picvector():
    klist = []
    def __init__(self, img):
        self.img = img
    def vectorpixels(self):
        global x
        global y
        self.im = Image.open(self.img) # open file from disk
        self.pixels = self.im.load() # list of pixels
        self.x, self.y = self.im.size # x y sizes picture
        for i in range(self.y):
            self.klist.append([0]*self.x)
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = self.pixels[i, j]
                self.pixels[i, j] = 255 - r, 255 - g, 255 - b
                self.klist[j][i] = self.pixels[i, j]
        #self.im.save(self.img + "-1" + ".jpg") # this option is optional
        return self.klist
    def hx(self):
        global x
        x = self.x
        return self.x
    def hy(self):
        global y
        y = self.y
        return self.y
