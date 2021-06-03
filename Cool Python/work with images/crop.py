from PIL import Image
img = Image.open("naruto.jpg")
img.show()
cropped = img.crop((100, 0, 500, 500))
cropped.show()