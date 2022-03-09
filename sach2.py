import collections
import ntpath as path
from csv import reader
import pandas as pd
import functools
import os
import csv
import sys

def compare_common_files_by_lines(directory_one):
   d1_files = set(os.listdir(directory_one))
   common_files = list(d1_files)
   if common_files:
     for filename in common_files:
        if filename.endswith('.csv'):
          file_01 = open(f'{directory_one}/{filename}', 'r', encoding='ISO-8859-1')
          #csv_file_01 = set(map(tuple, csv.reader(file_01)))
          #different = csv_file_01 ^ csv_file_02
          listt = []
          csv_reader = reader(file_01)
          next(csv_reader)
          for row in csv_reader:
             listt.append(path.basename(row[0]))
          return listt
          
dirt1 = '/home/ayuba/'
dirt2 = '/home/ayuba/newfolder2'

check = compare_common_files_by_lines(dirt1)
check2 = compare_common_files_by_lines(dirt2)

if collections.Counter(check) == collections.Counter(check2):
    print("it matches")
else:
    print("No joy!!!!!")
