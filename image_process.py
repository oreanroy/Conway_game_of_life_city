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
        self.img.resize((width, height), Image.ANTIALIAS)
        self.width = width
        self.height = height

    def convert_to_black(self):
        self.img = self.img.convert('1')
        #self.img.save('Resources/black_delhi2.png')

    def get_binary_arr(self):
        arr = []
        for i in range(self.height):
            col = []
            for j in range(self.width):
                pixel_rgb = self.img.load()[i,j]
                if pixel_rgb >= 180:
                    col.append(1)
                else:
                    col.append(0)
            arr.append(col)
        return arr




