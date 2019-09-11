This is a script to organize image and video files into subfolders based on the year that the image or video was taken. 

The script first tries to get the year from the exif data, but if that fails, it then does a regex search for the year in the filename. If the second step fails, then it leaves the file in place. 

Videos are also sorted, but because there isn't standard exif data to extract, a regex search looks for the year in the filename. If the search fails, the file is left in place.