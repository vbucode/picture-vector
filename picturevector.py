#module to work with pixels
from PIL import Image

class Picvector():
    klist = []
    slist = []
    xlist = []
    ylist = []
    def __init__(self, img):
        self.img = img
    def vectorpixels(self):
        global x
        global y
        self.im = Image.open(self.img) # open file from disk
        self.pixels = self.im.load() # list of pixels
        self.x, self.y = self.im.size # x y sizes picture
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = self.pixels[i, j]
                self.pixels[i, j] = 255 - r, 255 - g, 255 - b
                self.slist.append(self.pixels[i, j])
            self.klist.append(self.slist)
            del self.slist[self.x:]
        #self.im.save(self.img + "-1" + ".jpg") # this option is optional
        for i in self.klist:
            for j in i:
                if sum(j) <= 6:
                    self.ylist.append(0)
                self.ylist.append(1)
            self.xlist.append(self.ylist)
            del self.ylist[len(i):]
        return self.xlist
    def hx(self):
        global x
        x = self.x
        return self.x
    def hy(self):
        global y
        y = self.y
        return self.y
        
        
