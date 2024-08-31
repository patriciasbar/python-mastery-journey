from PIL import Image, ImageFilter

img = Image.open('./image_processing/pikachu.jpg')

edited_img = img.convert('L')
#edited_img.save("./image_processing/grey.png","PNG")

# resize = edited_img.resize((300, 300))
# resize.save("./image_processing/resized.png", "png")
# box = (100, 100, 400, 400)
# cropped = img.crop(box)
# cropped.save("./image_processing/crop.png","PNG")

img.thumbnail((400,200))

img.save
img.show()

