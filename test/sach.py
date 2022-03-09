import collections
import ntpath as path
from csv import reader
import pandas as pd
import functools 

def list_dat(dir):
   with open(dir, 'r') as read_obj:
       csv_reader = reader(read_obj)
       list = []
       next(csv_reader)
       for row in csv_reader:
          list.append(path.basename(row[0]))
       return list

dirt = '/home/ayuba/sample2.csv'

dirt2 = '/home/ayuba/sample.csv'


if collections.Counter(list_dat(dirt)) != collections.Counter(list_dat(dirt2)):
  print("It Match up")
else:
  print("No Joy!!!!!")
