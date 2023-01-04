#!./venv/bin/python

import os
import sys
from PIL import Image


class Resizer():
    def __init__(self, path):
        if not os.path.isfile(path):
            self.files = [os.path.join(path, item) for item in os.listdir(path) if os.path.isfile(os.path.join(path, item))]
        else:
            self.files = [path]

    def getNewSize(self, oldsize, width=0, height=0):
        if (width > 0):
            height = int(width / oldsize[0] * oldsize[1])
        else:
            width = int(height / oldsize[1] * oldsize[0])
        return (width, height)

    def resizeFile(self, file, maxwidth=0, maxheight=0):
        image = Image.open(file)
        if maxwidth > 0 and image.width > maxwidth:
            newSize = self.getNewSize(image.size, width=maxwidth)
            image = image.resize(newSize)
            image.save(file)
        elif maxheight > 0 and image.height > maxheight:
            newSize = self.getNewSize(image.size, height=maxheight)
            image = image.resize(newSize)
            image.save(file)

    def process(self, maxwidth=0, maxheight=0):
        for file in self.files:
            try:
                self.resizeFile(file, maxwidth, maxheight)
            except IOError:
                pass


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(sys.argv[0], "<directory|file> <width> <height>")
    else:
        msg = "WARNING:\nThis program will overwrite any image files "
        msg += "that exceed the given size in pixels, please make sure "
        msg += "that you have a backup.\n"
        msg += "Do you want to proceed? [yes/no]: "
        yesno = input(msg)
        if yesno.lower() == "yes":
            resizer = Resizer(sys.argv[1])
            resizer.process(maxwidth=int(sys.argv[2]), maxheight=int(sys.argv[3]))
        else:
            print("Nothing has been modified")