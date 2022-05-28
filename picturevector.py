from PIL import Image

class Picvector():
    def __init__(self, img):
        self.img = img
    def vectorpixels(self):
        klist = []
        self.im = Image.open(self.img) # open file from disk
        self.pixels = self.im.load() # list of pixels
        self.x, self.y = self.im.size # x y sizes picture
        for i in range(self.y):
            tlist = []
            tlist2 = []
            for j in range(self.x):
                r, g, b = self.pixels[j, i]
                self.pixels[j, i] = r, g, b
                if sum(self.pixels[j, i]) <= 700:
                    tlist.append([1])
                else:
                    tlist.append([0])
            for k in tlist:
                tlist2.extend(k)
            klist.append(tlist2)
        #self.im.save(self.img + "-1" + ".jpg") # this option is optional
        return klist
