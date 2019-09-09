import os
from PIL import Image

def get_date_taken(path):
    return Image.open(path)._getexif()[36867]

filepath = os.getcwd()

for file in os.listdir(filepath):
     print(file)

#TODO: Find all image files in top level folder

#TODO: Parse the strange filenames, changing them if need be

#TODO: Read image metadata, extract year

#TODO: Move file based on year
