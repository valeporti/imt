__author__ = 'lenca'

__author__ = 'lenca'
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%%cell 

str_beg = '\n----------------------------------------------------\n'
str_end = '\n                                ********************\n'


print ('\nData preparation\n')

# ##########################################################################
# Read the data
#
# The data file is a csv file
#
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
#
# 

df = pd.read_csv('datasets/tips.csv',  sep=',',header=0, encoding='utf-8')


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
# Let change the type of some variables
# Our data set seems to be ready... but it is not really
# So we have to prepare it before to analyze it!


# ##########################################################################
# Modify the data
#
# Change scale, recode variables, remove a variable, create a variable

#%% cell 
## add column categorical 
listofcategoricalvar = []
s = pd.Categorical(df.SEX, categories=[0,1]) ## define a categorical variable, 
s.rename_categories(["M","F"], inplace=True) #inplace : boolean (default: False) Whether or not to rename the categories inplace or return a copy of this categorical with renamed categories.
print (s.value_counts())
df["CAT_SEX"] = s
df["CAT_SEX"].astype('category')
listofcategoricalvar.append("CAT_SEX")

print (str_beg)
print ('Statistic summary')
print (df.describe())
print ('Two first rows:')
print (df[:2])
print (str_end)

#%% cell 

s = pd.Categorical(df.SMOKER, categories=[0,1])
s.rename_categories(["No","Yes"], inplace=True)
df["CAT_SMOKER"] = s
df["CAT_SMOKER"].astype('category')
listofcategoricalvar.append("CAT_SMOKER")

print (str_beg)
print ('Statistic summary')
print (df.describe())
print ('Two first rows:')
print (df[:2])
print (str_end)


#%%cell

s = pd.Categorical(df.DAY, categories=[3,4,5,6])
s.rename_categories(["Thu", "Fri", "Sat", "Sun"], inplace=True)
df["CAT_DAY"] = s
df["CAT_DAY"].astype('category')
listofcategoricalvar.append("CAT_DAY")

print (str_beg)
print ('Statistic summary')
print (df.describe())
print ('Two first rows:')
print (df[:2])
print (str_end)


#%% cell
s = pd.Categorical(df.TIME, categories=[0,1])
s.rename_categories(["Day", "Night"], inplace=True)
df["CAT_TIME"] = s
df["CAT_TIME"].astype('category')
listofcategoricalvar.append("CAT_TIME")

print (str_beg)
print ('Statistic summary')
print (df.describe())
print ('Two first rows:')
print (df[:2])
print (str_end)

#%% cell
# Do we need OBS? Not really so the column can be dropped to save memory
df.drop('OBS', inplace=True,axis=1)
print (str_beg)
print ('Statistic summary')
print (df.describe())
print ('Two first rows:')
print (df[:2])
print (str_end)

#%% cell 
# Finally we create the PTIPP
df["PTIP"] = 100 * df["TIP"] / df["BILL"]

print (df.describe())
print ('Two first rows:')
print (df[:2])
print (str_end)

# Let now see how looks our dataframe
print (str_beg)
print ('Dataframe information')
print (df.head())
print (df.info())
print (df.index)
print (df.columns)
print (df.dtypes)
print (str_end)


#%% cell 
# Show a quick statistic summary of the data
print (str_beg)
print ('Statistic summary')
print (df.describe())
print

print ('number of categorical values'), len(listofcategoricalvar)
for catvar in listofcategoricalvar:
	print (catvar + ':')
	print (df[catvar].value_counts())
print (str_end)
print
print ('OK, our data set seems now to be ready... let\'s go to analyze it!')
print
