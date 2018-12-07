__author__ = 'lenca'
# -*- coding: utf-8 -*-



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl
from statsmodels.graphics.mosaicplot import mosaic
#import histogram_functions as myhist
#from modify_data import *
#from histogram_functions import *
#from utils import *
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
# Show a quick statistic summary of the data
#
# 
#print str_beg
#print 'Statistic summary'
#print df.describe()
#print str_end
# As categorical attributes have integer values some statistics are not valid
# Remember Home Work --Scale of measurment-- and coding
# Let change the type of some variables
# Our data set seems to be ready... but it is not really
# So we have to prepare it before to analyze it!


# ##########################################################################
# Modify the data
#
# 

#listofcategoricalvar = modify_data(df)

# Let now see how looks our dataframe
#print str_beg
#print 'Dataframe information'
#print df.info()
#print df.index
#print df.columns
#print df.dtypes
#print str_end





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

#%%

#wait()


# ##########################################################################
# Let's look at some relations between values of variables
# Let's visualize some relations between values of variables
# 
#
# http://pandas.pydata.org/pandas-docs/stable/visualization.html
# https://plot.ly/
#
# To do: introduce Chi2?
#


# http://pandas.pydata.org/pandas-docs/stable/groupby.html

print (str_beg)
print ('Let\'s look at day and sex\n')
print
print (df.groupby("CAT_DAY").size()) # same as df["CAT_DAY"].value_counts()
print
print (df.groupby("CAT_SEX").size()) # same as df["CAT_SEX"].value_counts()
print

# Create a groupby variable that groups days by sex
groupby_day_sex = df.groupby(["CAT_DAY", 'CAT_SEX'])

print ('\n*** Analysis with groupby ***\n')
print('init sex size')
print (groupby_day_sex.size()) # print df.groupby(["CAT_DAY", 'CAT_SEX']).size()
print('init sex meqn')
print (groupby_day_sex.mean())  # df.groupby(["CAT_DAY", 'CAT_SEX']).mean()
print('fin sex meqn qnd size')

#%% cell

#print df.groupby(["CAT_DAY", 'CAT_SEX']).describe()

print ('\n*** Analysis with contingency table ***\n')
print (pd.crosstab(df['CAT_DAY'], df['CAT_SEX'], margins=True))
# with percentage
print (pd.crosstab(df['CAT_DAY'], df['CAT_SEX'], margins=True).apply(lambda r: r/len(df.index), axis=1))

#http://statsmodels.sourceforge.net/stable/genera ted/statsmodels.graphics.mosaicplot.mosaic.html
# Mosaic 
#http://stackoverflow.com/questions/27225636/how-to-create-mosaic-plot-from-pandas-dataframe-with-statsmodels-library
#http://stackoverflow.com/questions/31029560/plotting-categorical-data-with-pandas-and-matplotlib

fig_mos = mosaic(df, index=["CAT_DAY", 'CAT_SEX'])
plt.savefig('figures/mosaicplot-catdaysbycatsex'+'.pdf', dpi=100)
#pl.show()
plt.clf()

#%% cell

# Hum... males pay much more the bill during week-end... is there a 'gentlemen' biais
# Several ways to check this:
# print '\n Is there a gentlement biais on week-end?\n'
#print df.groupby(["CAT_DAY", 'CAT_SEX', 'SIZE']).size()
#print df.groupby(["SIZE", 'CAT_SEX', 'CAT_DAY']).size()
#print pd.crosstab([df['CAT_DAY'], df['CAT_SEX']], df['SIZE'], margins=True)
#print df['SIZE'].groupby([df['CAT_SEX'], df['CAT_DAY']]).size()
print (str_end)



print (str_beg)
print ('\n *** Percentage of tip by sex and smoker ***\n')

print (df['PTIP'].groupby([df['CAT_SMOKER'], df['CAT_SEX']]).size())
print (df['PTIP'].groupby([df['CAT_SMOKER'], df['CAT_SEX']]).mean())
print

## show count and mean in same table
print (df['PTIP'].groupby([df['CAT_SMOKER'], df['CAT_SEX']]).aggregate([len, np.mean, np.std]).reset_index())
print

# http://stackoverflow.com/questions/18620199/how-to-use-two-different-functions-within-crosstab-pivot-table-in-pandas?rq=1
meanptipspersomkerandsex = pd.crosstab(df['CAT_SMOKER'],df['CAT_SEX'], values=df['PTIP'], aggfunc=[len, np.mean], margins=True)
print (meanptipspersomkerandsex.reorder_levels([1,0], axis=1).sort_index(axis=1))
#print meanptipspersomkerandsex
print (str_end)

#%% cell
#############################################
print (str_beg)
print ('\n *** Percentage of tip by days and time ***\n')



print (df['PTIP'].groupby([df['CAT_DAY'], df['CAT_TIME']]).size())
print (df['PTIP'].groupby([df['CAT_DAY'], df['CAT_TIME']]).mean())
print


print (df['PTIP'].groupby([df['CAT_DAY'], df['CAT_TIME']]).aggregate([len, np.mean]).reset_index())
print

 #faire histo cummule (trouver un exemple)
 
df.boxplot(column='PTIP', by='CAT_DAY')
plt.savefig('figures/boxplot-ptip-by-day'+'.pdf', dpi=100)
df.boxplot(column='PTIP', by=['CAT_DAY', 'CAT_TIME'])
plt.savefig('figures/boxplot-ptip-by-day-and-time'+'.pdf', dpi=100)
#pl.show()

# http://stackoverflow.com/questions/18620199/how-to-use-two-different-functions-within-crosstab-pivot-table-in-pandas?rq=1
meanptipsperdayandtime = pd.crosstab(df['CAT_DAY'],df['CAT_TIME'], values=df['PTIP'], aggfunc=[len, np.mean], margins=True)
print (meanptipsperdayandtime.reorder_levels([1,0], axis=1).sort_index(axis=1))
#print meanptipsperdayandtime
print (str_end)

#%% cell
# Percentage of tip by size of the party
#
print (str_beg)
print ('\n *** Percentage of tip by size of the party ***\n')

print (df['PTIP'].groupby([df['SIZE']]).mean())

groupptippersize = df['PTIP'].groupby([df['SIZE']])

# We can apply multiple functions at once
print (groupptippersize.agg([len, np.sum, np.mean, np.std]))
print (str_end)
#wait()
#


# Many other analysis can be done...
#
#print df.groupby(["CAT_TIME", 'CAT_DAY']).size()
#print df.groupby(["CAT_DAY", 'CAT_TIME']).size()
#print df.groupby(["CAT_TIME", 'CAT_DAY']).mean()
#df.boxplot(column='BILL', by='CAT_DAY') #faire histo cummule
#
#df.boxplot(column="BILL",by="CAT_DAY")
#plt.savefig('figures/boxplot bill by cat_days'+'.pdf', dpi=100)
#df.plot.scatter(x='SIZE', y='BILL');
#plt.show(


print
# http://chrisalbon.com/python/pandas_crosstabs.html
print ('\nContingency tables\n')
#print pd.crosstab(df['CAT_SEX'], df['CAT_SMOKER'], margins=True)
print
print ('\n *** Contingency smoker by sex and day ***\n')
print (pd.crosstab([df['CAT_SEX'],df['CAT_DAY']], df['CAT_SMOKER'], margins=True))
print (pd.crosstab([df['CAT_SEX'],df['CAT_DAY']], df['CAT_SMOKER'], margins=True).apply(lambda r: r/len(df.index), axis=1))

print ('\n *** Who and when pay large tip? ***\n')
print (pd.crosstab(df['CAT_SEX'], df['TIP'] > 7.0, margins=True))
print (pd.crosstab([df['CAT_SEX'],df['CAT_DAY']], df['TIP'] > 7.0, margins=True))
print (pd.crosstab([df['CAT_DAY']], df['TIP'] > 7.0, margins=True))
#calculate for values bigger than 2*mean
print (pd.crosstab([df['CAT_DAY']], df['TIP'] > 2* df['TIP'].mean(), margins=True))

print ('\n *** Who and when pay large percentage of tip? ***\n')

print (pd.crosstab([df['CAT_DAY'], df['CAT_SEX']], df['PTIP'] > 2* df['PTIP'].mean(), margins=True))

print (str_end)




# ##########################################################################
# Let's look at some correlations between variables
# Let's visualize some correlations between variables
# 
#
# To do: introduce difference of means (and statistical test) next year

print (str_beg)
print ('\n*** Correlation BILL and TIP ***\n')
df.plot.scatter(x='BILL', y='TIP');
print (df[['BILL', 'TIP']].corr(method='pearson')) # Plots the matrix
print (df['BILL'].corr(df['TIP'], method='pearson'))
# #Do it with a pandas regression to get the p value from the F-test
# cf http://stackoverflow.com/questions/25571882/pandas-columns-correlation-with-statistical-significance


print ('\n *** Correlation matrix, BILL, TIP, PTIP and SIZE ***\n')
print (df[['BILL', 'TIP', 'PTIP', 'SIZE']].corr(method='pearson')) # Plots the matrix
# Negative corr BILL and PTIP (remove the outliers to see)
# Positive corr BILL and TIP (expected!)
# Negative corr SIZE and PTIP (remove the outliers to see)
# Positive corr SIZE and BILL (expected but it is not so strong, look at outliers):

print ('\n *** Bill by size of the party ***\n')
print (df['BILL'].groupby([df['SIZE']]).mean())
grouppbillpersize = df['BILL'].groupby([df['SIZE']])
print (grouppbillpersize.agg([len, np.sum, np.min, np.mean, np.std, np.max]))
df.boxplot(column='BILL', by='SIZE')
plt.savefig('figures/boxplot-bill-by-size'+'.pdf', dpi=100)
print


df.plot.scatter(x='BILL', y='PTIP');
plt.savefig('figures/scatter-bill-by-ptip'+'.pdf', dpi=100)

df.plot.scatter(x='SIZE', y='PTIP');
plt.savefig('figures/scatter-size-by-ptip'+'.pdf', dpi=100)
df.boxplot(column='PTIP', by='SIZE');
plt.savefig('figures/boxplot-ptip-by-size'+'.pdf', dpi=100)

# Other plots can be drawn
# For example df.boxplot(column="BILL", by="CAT_DAY")
# plt.savefig('figures/boxplot bill by cat_days'+'.pdf', dpi=100)

#plt.show()

wait()

print (str_end)

df.boxplot(column="PTIP",by="SIZE")
#plt.show()

exit()





print
print ('-----------------------------------------------------')
print ('End of multivariate analysis introduction')
print ('Let''s now compute our first model.')
print ('-----------------------------------------------------')
print
