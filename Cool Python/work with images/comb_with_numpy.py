from PIL import Image
import numpy as np

arr = np.zeros([150,300], dtype=np.uint8)
#Set grey value to black or white depending on x position
for x in range(300):
    for y in range(150):
        if (x % 16) // 8 == (y % 16)//8:
            arr[y, x] = 0
        else:
            arr[y, x] = 255
img = Image.fromarray(arr)
img.show()