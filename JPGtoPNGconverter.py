import sys
import os
from PIL import Image, ImageFilter


#grab first and second arguemnet
image_folder = sys.argv[1]
ouput_folder = sys.argv[2]


# #check if new exits if not create it
if not os.path.exists(ouput_folder):
    os.makedirs(ouput_folder)


#open existing folder and save files in PNG format
for filename in os.listdir(image_folder):
    im = Image.open(f"{image_folder}{filename}")
    clean_name = os.path.splitext(filename)[0]
    im.save(f"{ouput_folder}{clean_name}.png", "png")






