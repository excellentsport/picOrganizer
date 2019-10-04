import os
import re
import argparse
from PIL import Image

# TODO: add argparse.ArgumentParser to designate WD. Consider option --dry-run.


# get the year
def year_taken(path):
    date_taken = Image.open(path)._getexif()[36867]
    return date_taken[0:4]


# using the year data from the image, check if a folder exists.
# If not, then create it. Move the file to the folder.
def sort_file(file_name, year_photo_taken):
    if not os.path.exists(year_photo_taken):
        os.makedirs(year_photo_taken)
    os.rename(file_name, year_photo_taken + '\\' + file_name)
    print(file_name + ' moved.')


def main():

    # Process images
    for file_name in os.listdir(file_path):
        if file_name.endswith(IMAGE_TYPES):  # 'endswith() can be fed a tuple.
            try:
                # Try to get the 'date taken' image, lack of info throws an exception.
                year = year_taken(file_name)
                sort_file(file_name, year)
            except:
                # If 'date taken' not in exif data, get the year from the file name
                print('Date taken not found in exif data for ' + file_name + '.')
                regex_match = year_regex.search(file_name)

                if regex_match is None:
                    # if you can't find year in the file name, leave it alone.
                    print('Year not found in filename for ' + file_name + ', file not moved.')
                else:
                    year = regex_match.group()
                    sort_file(file_name, year)

    # Process videos
    for file_name in os.listdir(file_path):
        if file_name.endswith(VIDEO_TYPES):

            try:
                # No exif data in videos - do a regex search for year in the file name
                regex_match = year_regex.search(file_name)
                if regex_match is None:
                    # If a year isn't found, then leave the file there to be manually sorted.
                    print('Year not found in filename for ' + file_name + ', file not moved.')
                else:
                    year = regex_match.group()
                    sort_file(file_name, year)
            except:
                print('Unable to sort ' + file_name + '.')

def dir_path_check(string):
    """Checks if user entered string is a valid folder path"""
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

def parse_args():
    parser = argparse.ArgumentParser(description='Iterate through folder to sort images and media')
    parser.add_argument('-d', '--dryrun', description = 'Do a dry run of the file sorting',default=False)
    parser.add_argument('--path', type=dir_path_check, description = 'Folder path of files',default=os.getcwd())
    #TODO: Finish me!

# TODO: Deal with setting up the three options below to work based on user arguments
file_path = args.path
file_path = os.getcwd()
file_path = os.path.join(os.path.expanduser('~'), "Dropbox", "Camera Uploads")  # os.path.expanduser('~') gets the path for the user's home folder.
os.chdir(file_path) #TODO: Why did the directory need to be changed to the different file path? Is this necessary for all non-script paths?

# define what image and video types to search for
IMAGE_TYPES = ('.png', '.jpeg', '.jpg', '.gif')
VIDEO_TYPES = ('.mov', 'mp4')

# Search for 4 digit string starting with '20'
year_regex = re.compile(r'20(\d){2}')


if __name__ == "__main__":
    main()
