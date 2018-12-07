# coding: utf-8

__author__ = 'lenca'

__author__ = 'lenca'


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



str_beg = '\n----------------------------------------------------\n'
str_end = '\n                                ********************\n'

# ##########################################################################
# Read the data and create the dataframe
#
# The data file is a csv file
#
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
#
# 

df = pd.read_csv('datasets/tips.csv',  sep=',', header=0, encoding='utf-8')

# ##########################################################################
# Get information about the data
#
# See data set, part of data set, number of raws and columns,
# type of attributes, basic statistics

# http://pandas.pydata.org/pandas-docs/version/0.18.1/10min.html#min
#
# 


print (str_beg)
print ('Top & bottom rows of the dataframe\n')
print (df.head()) #df.head(n), default n=5
print (df.tail()) #df.tail(n), default n=5
print (str_end)
print
print (str_beg)
print ('Dataframe information\n')
print ('\n -- dataframe info\n')
print (df.info())
print ('\n -- dataframe index\n')
print (df.index)
print ('\n -- dataframe columns\n')
print (df.columns)
print ('\n -- dataframe types\n')
print (df.dtypes)
print (str_end)


# ##########################################################################
# Access the data
#

# http://pandas.pydata.org/pandas-docs/stable/indexing.html
#
#
print
print (df)
print (str_beg)
# Access to sub-part of an array with slicing
print ('From row 1 to the end')
print (df[1:])
# Print the rows 0 (included) to 2 (excluded): the 2 first rows 0 and 1
print ('Two first rows:')
print (df[:2])

print ('Rows 4 to 6:')
print (df[4:7])
print ('Last row:')
print (df[len(df.index)-1:])


# Print value of dimension 2 (BILL) for observation 5 
##print ('Value of dataset[4][1]: ') + str(df.loc[4,'totbill'])  compiling error with '+'
print ('Value of dataset[4][1]: ') 
str(df.loc[4,'totbill'])

print (str_beg)
print ('Print a column\n')
print (df["sex"]) # same as print df.SEX
print (str_end)



# ##########################################################################
# Show a quick statistic summary of the data
#
# 
print (str_beg)
print ('Statistic summary')
print (df.describe())
print (str_end)
# As categorical attributes have integer values some statistics are not valid
# Remember Home Work --Scale of measurment--
# We will change the type of some variables



print
print ('Our data set seems to be ready... let\'s go to analyze it!')
print

