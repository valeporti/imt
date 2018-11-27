import pandas as pd
from pylab import *

#import os
#import re
#pattern = re.compile('\t')
#if os.path.exists('./tips_dataset.txt'):
#        f = open('./tips_dataset.txt')
#        for line in f:
#                match = pattern.match('')
#                print(match)
#        f.close()

columns = ['OBS', 'BILL', 'TIP', 'SEX', 'SMOKER', 'DAY', 'TIME', 'SIZE']
path = './tips_dataset.txt'
frame = pd.read_table(path, sep='\s+', lineterminator='\n', names=columns)

table = frame.pivot_table(index='SEX', values='TIP',columns=['DAY'],aggfunc=sum)
table.plot(title='Total of births by year and by sex', kind='pie', subplots=1)
show()
print(table)