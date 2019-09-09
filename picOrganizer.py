import os
from PIL import Image

def get_date_taken(path):
    return Image.open(path)._getexif()[36867]

def sortfile(filename,yeartaken):
    #TODO write this function

filepath = os.getcwd()

for file in os.listdir(filepath):
    if file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".jpg"):
        fullpath = filepath + "\\" + file
        print(fullpath)
        
        try:
            fulldate = get_date_taken(file)
            year = fulldate[0:4]
            sortfile(file,year)
        except:
            year = None
            sortfile(file,year)
