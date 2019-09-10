import os, time, re
from PIL import Image

def get_date_taken(path):
    return Image.open(path)._getexif()[36867]

def sortfile(filename,yeartaken):
    if not os.path.exists(yeartaken):
        os.makedirs(yeartaken)
    os.rename(filename,yeartaken+'\\'+filename)
    print(filename + ' moved.')

imagetypes = ('.png', '.jpeg', '.jpg', '.gif')
videotypes = ('.mov', 'mp4')

yearRegex = re.compile(r'20(\d){2}')

#filepath = os.getcwd()
filepath = os.path.expanduser('~') + '\\Dropbox\\Camera Uploads'
print(filepath)

#process images
for file in os.listdir(filepath):
    if file.endswith(imagetypes):
        fullpath = filepath + '\\' + file  
        try:
            fulldate = get_date_taken(file)
            year = fulldate[0:4] #standard output date is year first.
            sortfile(file,year)
        except:
            print('Date taken not found in exif data for ' + file + '.')
            regexMatch = yearRegex.search(file)
            year = regexMatch.group()
            if year is None:
                print('Year not found in filename for ' + file + ', file not moved.')
            else:
                sortfile(file,year)

#process videos
for file in os.lisdir(filepath):
    if file.endwith(videotypes):
        fullpath = filepath + "\\" + file

        try:
            regexMatch = yearRegex.search(file)
            year = regexMatch.group()
            if year is None:
                print('Year not found in filename for ' + file + ', file not moved.')
            else:
                sortfile(file,year)
        except:
            print('Unable to sort ' + file + '.')