__author__ = 'lenca'

__author__ = 'lenca'
# -*- coding: utf-8 -*-



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl
#from statsmodels.graphics.mosaicplot import mosaic
#import histogram_functions as myhist
#from modify_data import *
##from histogram_functions import *
#from utils import *



import os
import numpy as np
import pandas as pd
from sklearn import metrics # for confusion matrix and ROC curve
import matplotlib.pyplot as plt
import requests
import io



str_beg = '\n----------------------------------------------------\n'
str_end = '\n                                ********************\n'

# ##########################################################################
# Read the data
#
# The data file is a csv file
#
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
#
# 

df = pd.read_csv('datasets/tips.csv',  sep=',', header=0, encoding='utf-8')


# ##########################################################################
# Modify the data
#
# 

#listofcategoricalvar = modify_data(df)

##########@









# ##########################################################################
# Modify the data
#
# Change scale, recode variables, remove a variable, create a variable

#%% cell 1
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

#%% cell 2

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


#%%%cell
# ##########################################################################
# Let now see how looks our dataframe
#
#
#print str_beg
#print 'Dataframe information'
#print df.info()
#print df.index
#print df.columns
#print df.dtypes
#print str_end


# ##########################################################################
# Show a quick statistic summary of the data
#
# 
print ('Statistic summary')
print('--------ici--------')
print (df.describe())
print
print (df["CAT_SEX"].value_counts())
print (df["CAT_SMOKER"].value_counts())
print (df["CAT_DAY"].value_counts())
print (df["CAT_TIME"].value_counts())
print (str_end)
print

# Descriptive statistics 
# http://www.socialresearchmethods.net/kb/statdesc.php
# https://www3.nd.edu/~rwilliam/stats1/

#wait()




# ##########################################################################
# Let's compute and visualize the values of variables (univariate analysis)
#
# http://pandas.pydata.org/pandas-docs/stable/visualization.html
# https://plot.ly/
# http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.hist
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.hist.html#pandas.DataFrame.hist
#
#

#%% cell 
#
# Days distribution
#
print (str_beg)
print (' Days distribution')
dd = df['CAT_DAY'].value_counts(sort=False)
print (dd)
fig_dd = dd.plot(kind='bar') #df['CAT_DAY'].value_counts(sort=False).plot(kind='bar')
plt.title('Days distribution')
plt.savefig('figures/bar_days_distribution'+'.pdf', dpi=100)
#plt.show(fig_dd)
plt.clf() # Need to close the current figure, otherwise strange behaviour of next figure


fig_dd = dd.plot(kind='pie') #df['CAT_DAY'].value_counts(sort=False).plot(kind='bar')
plt.title('Days distribution')
plt.savefig('./figures/pie_days_distribution'+'.pdf', dpi=100)
#plt.show(fig_dd)
plt.clf() # Need to close the current figure, otherwise strange behaviour of next figure


#%% cell 
#
# Sex distibution
#
print (' Sex distribution')
sx = df['CAT_SEX'].value_counts(sort=False)
print (sx)

# try also 'bar' instead of 'pie'
plt.title('Sex distribution')
fig_sx = sx.plot(kind='pie') #
plt.savefig('./figures/pie_sex_distribution'+'.pdf', dpi=100)
#plt.show(fig_sx)
plt.clf()  # Need to close the current figure, otherwise strange behaviour of next figure
print (str_end)

#%% cell 
#
# Distribution BILL
# 

print ('\nHistogram BILL\n')
bins_list = []
bins_width = 5 # 5 dollars
## range range([start], stop[, step])
for bins_number in range(0,60,bins_width):
	bins_list.append(bins_number)
print (bins_list, len(bins_list))
fig_histBILL = plt.hist(df.BILL, bins=bins_list, normed=0, histtype='bar', rwidth=1.0, align='mid')
plt.xlabel('BILL')
plt.ylabel('Count')
plt.title('Histogram of BILL (' + str(bins_width) + '$\$$ bin size)')
plt.savefig('figures/histogram_bill_'+str(bins_width)+'.pdf', dpi=100)
#plt.show(fig_histBILL)
plt.clf() 
#wait()


#plot_histogram(df.BILL, 1.0, 'BILL', 'Count', '$\$$')
#plot_histogram(df.BILL, 5.0, 'BILL', 'Count', '$\$$')

#%% cell 
#plt.xlabel('BILL')
#plt.ylabel('')
#As a float, determines the reach of the whiskers to the beyond the first and third quartiles. 
#In other words, where IQR is the interquartile range (Q3-Q1), 
#the upper whisker will extend to last datum less than Q3 + whis*IQR).
# Similarly, the lower whisker will extend to the first datum greater than Q1 - whis*IQR. 
plt.title('Boxplot of BILL (1.5 IQR)')
df.boxplot(column="BILL", return_type='axes', sym = 'bo', whis=1.5)
plt.savefig('./figures/boxplot_bill_IQR15'+'.pdf', dpi=100)
plt.clf() 

plt.title('Boxplot of BILL (2 IQR)')
df.boxplot(column="BILL", return_type='axes', sym = 'bo', whis=2)
plt.savefig('./figures/boxplot_bill_IQR2'+'.pdf', dpi=100)
plt.clf() 
print ('BILL: outliers?')
print (df[df.BILL>45.68])

#%% cell 
#
# Distribution TIP
#
### range range([start], stop[, step])
bins = []
bins_width = 1 # 1 dollar
for bins_number in range(0,11,bins_width):
	bins.append(bins_number)
print ('\nHistrogam TIP'+str(bins_width)+'\n')
print (bins, len(bins))
plt.xlabel('TIP')
plt.ylabel('Count')
plt.title('Histogram of TIP ($\$$' + str(bins_width) + ' bin size)')
fig_histTIP = plt.hist(df.TIP, bins=bins, normed=0, histtype='bar', rwidth=1.0, align='mid')
plt.savefig('./figures/histogram_tip_'+str(bins_width)+'.pdf', dpi=100)
#plt.show(fig_histTIP)
plt.clf() 

#%% cell 
#notre implemenqttion

s = pd.Categorical(df.TIP, categories=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
s.rename_categories([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], inplace=True)
df["CAT_TIP"] = s
df["CAT_TIP"].astype('category')
listofcategoricalvar.append("CAT_TIP")

tip = df['CAT_TIP'].value_counts(sort=False)
print (tip)

# try also 'bar' instead of 'pie'
plt.title('Tip distribution')
fig_tip = tip.plot(kind='pie') #
plt.savefig('./figures/pie_tip_distribution'+'.pdf', dpi=100)



#plot_histogram(df.TIP, 0.1, 'TIP', 'Count', '$\$$', save=True, date=False)
#plot_histogram(df.TIP, 1.0, 'TIP', 'Count', '$\$$', save=True)

#%% cell 
#
# Distribution of PTIP
#

#plot_histogram(df.PTIP, 1.0, 'PTIP', 'Count', '%',save=True)
#plot_histogram(df.PTIP, 5.0, 'PTIP', 'Count', '%',save=True)

bins = []
bins_width = 2 # 1 dollar
for bins_number in range(0,73,bins_width):
	bins.append(bins_number)
print ('\nHistrogam PTIP'+str(bins_width)+'\n')
print (bins, len(bins))
plt.xlabel('PITP')
plt.ylabel('Count')
plt.title('Histogram of PTIP ($\$$' + str(bins_width) + ' bin size)')
fig_histTIP = plt.hist(df.PTIP, bins=bins, normed=0, histtype='bar', rwidth=1.0, align='mid')
plt.savefig('./figures/histogram_ptip_'+str(bins_width)+'.pdf', dpi=100)
#plt.show(fig_histTIP)
plt.clf() 

#%% cell 
plt.title('Boxplot of PTIP (2 IQR)')
df.boxplot(column="PTIP", return_type='axes', sym = 'bo', whis=2)
plt.savefig('figures/boxplot_ptip_IQR2'+'.pdf', dpi=100)
plt.clf() 

plt.title('Boxplot of PTIP (3 IQR)')
df.boxplot(column="PTIP", return_type='axes', sym = 'bo', whis=3)
plt.savefig('./figures/boxplot_ptip_IQR3'+'.pdf', dpi=100)
plt.clf() 

print ('Outliers?')
print (df[df.PTIP>35])



print (str_end)



print
print ('-----------------------------------------------------')
print ('End of univariate analysis introduction')
print ('Let''s know look at some relations between variables.')
print ('-----------------------------------------------------')
print
