from image_process import image

img = image('../Resources/delhi_img.PNG')
print(img.width)
print(img.height)
img.convert_to_black()
img.compress(100, 100)
print(img.width)
print(img.width)
print(img.get_binary_arr())
