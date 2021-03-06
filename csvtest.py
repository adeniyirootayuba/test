import os
import csv
import sys
from os import listdir

def compare_common_files_by_lines(directory_one, directory_two):
   d1_files = set(os.listdir(directory_one))
   d2_files = set(os.listdir(directory_two))
   common_files = list(d1_files & d2_files)
   check1 = find_csv_filenames(directory_one)
   check2 = find_csv_filenames(directory_two)
   if check1 != check2:
      print("Files doesn't match")
      sys.exit(1)
   for filename in common_files:
       if filename.endswith('.csv'):
          file_01 = open(f'{directory_one}/{filename}', 'r', encoding='ISO-8859-1')
          file_02 = open(f'{directory_two}/{filename}', 'r', encoding='ISO-8859-1')
          csv_file_01 = set(map(tuple, csv.reader(file_01)))
          csv_file_02 = set(map(tuple, csv.reader(file_02)))
          different = csv_file_01 ^ csv_file_02
          for row in sorted(different, key=lambda x: x, reverse=True):
             if row:
                return False
                        

def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]

dirt1 = '/home/ayuba/newfolder'
dirt2 = '/home/ayuba/newfolder2'

check = compare_common_files_by_lines(dirt1, dirt2)

if check == False:
   print("False")
else:
   print("We've got a match")