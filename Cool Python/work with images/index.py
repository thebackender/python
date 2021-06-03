from PIL import Image
im = Image.open("asset.jpg")
im.thumbnail((500, 500))
"""
#resize
try:
    im.thumbnail((500, 500))
    im.show()
except Exception():
    pass
"""

"""
#rotate
im = im.rotate(45)
im.show()
"""

#im.save('new.png')
#print(im.size)

"""
r, b, g = im.split()
im2 = Image.merge("RGB", (b, g, r))
im2.show()
"""

print(im)