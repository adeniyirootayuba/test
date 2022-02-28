import os
import csv
import sys

def compare_common_files_by_lines(dir1, dir2):
   csv_file1 = set(os.listdir(dir1))
   csv_file2 = set(os.listdir(dir2))
   
   if csv_file1 != csv_file2:
      print("Files name are not the samee")
      sys.exit(1)
   else:
      common_files = list(csv_file1 & csv_file2)
      if common_files:
        for filename in common_files:
           if filename.endswith('.csv'):
             file_01 = open(f'{dir1}/{filename}', 'r', encoding='ISO-8859-1')
             file_02 = open(f'{dir2}/{filename}', 'r', encoding='ISO-8859-1')
             csv_1 = set(map(tuple, csv.reader(file_01)))
             csv_2 = set(map(tuple, csv.reader(file_02)))
             different = csv_1 ^ csv_2
             for row in sorted(different, key=lambda x: x, reverse=True):
                if row:
                   return False      

dir1 = '/home/ayuba/newfolder'
dir2 = '/home/ayuba/newfolder2'

check = compare_common_files_by_lines(dir1, dir2)


if check == False:
   print("Doesnt match")
else:
   print("It match")
