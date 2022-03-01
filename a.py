from os import listdir
import os

def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    for filename in filenames:
	if filename.endswith(suffix):
           return str(filename)


    
#return [ filename for filename in filenames if filename.endswith( suffix ) ]


dir = '/home/ayuba/newfolder'
dir2 = '/home/ayuba/newfolder2'

check = os.path.isdir(dir)

if check == True and find_csv_filenames(dir) == find_csv_filenames(dir2):
	print("its the same "+ find_csv_filenames(dir) + " and " + find_csv_filenames(dir2))
else:
	print("No match " + find_csv_filenames(dir) + " and " + find_csv_filenames(dir2))

