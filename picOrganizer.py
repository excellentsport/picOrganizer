import os, time, re
from PIL import Image

#get the year 
def get_date_taken(path):
    dateTaken = Image.open(path)._getexif()[36867]
    return dateTaken[0:4]

#using the year data from the image, check if a folder exists. If not, then create it. Move the file to the folder.
def sortfile(filename,yeartaken):
    if not os.path.exists(yeartaken):
        os.makedirs(yeartaken)
    os.rename(filename,yeartaken+'\\'+filename)
    print(filename + ' moved.')

#define what image and video types to search for
imagetypes = ('.png', '.jpeg', '.jpg', '.gif')
videotypes = ('.mov', 'mp4')

yearRegex = re.compile(r'20(\d){2}') #Search for 4 digit string starting with '20'

#You can either place this script in the folder to sort, or you can manually 
#specify which directory you want. #To organize the script directory, comment 
#out the second two lines of code in this block. To organize a specific directory, 
#comment out the first line of code in this block.
filepath = os.getcwd()
#filepath = os.path.expanduser('~') + '\\Dropbox\\Camera Uploads' #os.path.expanduser('~') gets the path for the user's home folder.
#os.chdir(filepath)

#Process images
for file in os.listdir(filepath):
    if file.endswith(imagetypes):  # 'endswith() can be fed a tuple.
        try: #Try to get the 'date taken' data from an image file, if it doesn't have this info, it throws an exception.
            year = get_date_taken(file)
            sortfile(file,year)
        except: #When "date taken" isn't found in exif data, get the year from the filename
            print('Date taken not found in exif data for ' + file + '.')
            regexMatch = yearRegex.search(file)
            
            if regexMatch is None: #if you can't find a year in the filename, leave it alone to be manually sorted.
                print('Year not found in filename for ' + file + ', file not moved.')
            else:
                year = regexMatch.group()
                sortfile(file,year)

#Process videos
for file in os.listdir(filepath):
    if file.endswith(videotypes):

        try: #There isn't exif data in videos, so do a regex search for the year in the filename
            regexMatch = yearRegex.search(file)
            if regexMatch is None: #If a year isn't found, then leave the file there to be manually sorted.
                print('Year not found in filename for ' + file + ', file not moved.')
            else: 
                year = regexMatch.group()
                sortfile(file,year)
        except:
            print('Unable to sort ' + file + '.')