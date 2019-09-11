import os
import re
from PIL import Image

# TODO: add argparse.ArgumentParser to designate WD. Consider option --dry-run.


# get the year
def year_taken(path):
	date_taken = Image.open(path)._getexif()[36867]
	return date_taken[0:4]


# using the year data from the image, check if a folder exists.
# If not, then create it. Move the file to the folder.
def sort_file(file_name, year_taken):
	if not os.path.exists(year_taken):
		os.makedirs(year_taken)
	os.rename(file_name, year_taken+'\\'+file_name)
	print(file_name + ' moved.')


# define what image and video types to search for
image_types = ('.png', '.jpeg', '.jpg', '.gif')
video_types = ('.mov', 'mp4')

# Search for 4 digit string starting with '20'
year_regex = re.compile(r'20(\d){2}')

# You can either place this script in the folder to sort, or you can manually
# specify which directory you want. To organize the script directory, comment
# out the second two lines of code in this block. To organize a specific directory,
# comment out the first line of code in this block.
file_path = os.getcwd()
# file_path = os.path.join(os.path.expanduser('~'), "Dropbox", "Camera Uploads")  # os.path.expanduser('~') gets the path for the user's home folder.
# os.chdir(file_path)


def main():
	
	# Process images
	for file_name in os.listdir(file_path):
		if file_name.endswith(image_types):  # 'endswith() can be fed a tuple.
			try:
				# Try to get the 'date taken' data from image, lack of info throws an exception.
				year = year_taken(file_name)
				sort_file(file_name, year)
			except:
				# When 'date taken' isn't found in exif data, get the year from the file name
				print('Date taken not found in exif data for ' + file_name + '.')
				regex_match = year_regex.search(file_name)

				if regex_match is None:
					# if you can't find year in the file name, leave it alone.
					print('Year not found in file name for ' + file_name + ', file not moved.')
				else:
					year = regex_match.group()
					sort_file(file_name, year)
	
	# Process videos
	for file_name in os.listdir(file_path):
		if file_name.endswith(video_types):
	
			try:
				# No exif data in videos - do a regex search for year in the file name
				regex_match = year_regex.search(file_name)
				if regex_match is None:
					# If a year isn't found, then leave the file there to be manually sorted.
					print('Year not found in file name for ' + file_name + ', file not moved.')
				else:
					year = regex_match.group()
					sort_file(file_name, year)
			except:
				print('Unable to sort ' + file_name + '.')


if __name__ == "__main__":
	main()
