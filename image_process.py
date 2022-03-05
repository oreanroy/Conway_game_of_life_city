from turtle import width
from PIL import Image

# read a image
# compress the image
# get 1/0 arr of image

class image:

    def __init__(self, path):
        self.img = Image.open(path)
        self.width, self.height = self.img.size


    # compress the image to this width
    def compress(self, width, height):
        self.img = self.img.resize((width, height), Image.ANTIALIAS)
        self.width, self.height = self.img.size
        #self.height = height
        self.img.save('Resources/compressed_delhi2.png')

    def convert_to_black(self):
        self.img = self.img.convert('1')
        #self.img.save('Resources/black_delhi2.png')

    def get_binary_arr(self):
        arr = []
        width, height = self.img.size
        #print(f"height {height}, width {width}")
        for i in range(height):
            col = []
            for j in range(width):
                #print(f"this is i {i}, this is j {j}")
                pixel_rgb = self.img.load()[j,i]
                if pixel_rgb >= 180:
                    col.append(1)
                else:
                    col.append(0)
            arr.append(col)
        return arr




