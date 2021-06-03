from PIL import Image
image1 = Image.open("asset.jpg")
image2 = Image.open("naruto.jpg")

image1 = image1.resize((300, 300))
image2 = image2.resize((200, 300))
image1_size = image1.size
image2_size = image2.size
#create new image without content
new_image = Image.new('RGB', (image1_size[0] + image2_size[0], image1_size[1]), (250,250,250))
new_image.paste(image1, (0, 0))
new_image.paste(image2, (image1_size[0], 0))
new_image.show()