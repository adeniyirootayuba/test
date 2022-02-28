import os
import csv
import sys

def compare_common_files_by_lines(directory_one, directory_two):
   d1_files = set(os.listdir(directory_one))
   d2_files = set(os.listdir(directory_two))
   
   if d1_files != d2_files:
      print("Files name are not the samee")
      sys.exit(1)
   else:
      common_files = list(d1_files & d2_files)
      if common_files:
        for filename in common_files:
           if filename.endswith('.csv'):
             file_01 = open(f'{directory_one}/{filename}', 'r', encoding='ISO-8859-1')
             file_02 = open(f'{directory_two}/{filename}', 'r', encoding='ISO-8859-1')
             csv_file_01 = set(map(tuple, csv.reader(file_01)))
             csv_file_02 = set(map(tuple, csv.reader(file_02)))
             different = csv_file_01 ^ csv_file_02
             for row in sorted(different, key=lambda x: x, reverse=True):
                if row:
                     print(f'This row: \n {row} \n was different between the file {filename} in the directories'
                             f' {directory_one} and {directory_two}')
      

dir1 = '/home/ayuba/newfolder'
dir2 = '/home/ayuba/newfolder2'

check = compare_common_files_by_lines(dir1, dir2)
