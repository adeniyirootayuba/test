import os


dir = '/home/ayuba/newfolder'
check = os.path.exists(os.path.join(os.getcwd(), dir, 'test1.csv'))
print(check)
print(os.path.join(os.getcwd(), dir, 'test1.csv'))
