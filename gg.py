import filecmp
import os.path

def compare_red_drop_folder(first_path, second_path):


    compare_folder = filecmp.dircmp(first_path, second_path)
    if len(compare_folder.left_only)>0 or len(compare_folder.right_only)>0 or \
        len(compare_folder.funny_files)>0:
        return False
    (_, mismatch, errors) =  filecmp.cmpfiles(
        first_path, second_path, compare_folder.common_files, shallow=False)
    if len(mismatch)>0 or len(errors)>0:
        return False
    for the_same in compare_folder.common_dirs:
        directory1 = os.path.join(first_path, the_same)
        directory2 = os.path.join(second_path, the_same)
        if not compare_red_drop_folder(directory1, directory2):
            return False
    return True


pp = compare_red_drop_folder('/home/ayuba/newfolder', '/home/ayuba/newfolder2')
if pp == True:
   print('The files are the same')
else:
   print('The files doesnt match')
