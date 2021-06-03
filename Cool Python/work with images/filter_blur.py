from PIL import Image, ImageFilter
img = Image.open("naruto.jpg")
img.thumbnail((500, 500))
#img.filter(ImageFilter.BLUR).show()
#img.filter(ImageFilter.BoxBlur(5)).show()
img.filter(ImageFilter.GaussianBlur(3)).show()