# import useful libraries
import pandas as pd  # to manipulate dataframes, plots, ..
import matplotlib.pyplot as plt
import seaborn as sns # seaborn is an advanced library for visualization
import numpy as np
import scipy as sp

# the code below loads the data 
data_tips=pd.read_csv('datasets/tips.csv',  sep=',',header=0, encoding='utf-8')

 #df = pd.read_csv('datasets/tips.csv',  sep=',', header=0, encoding='utf-8')


# you can run the below code to see the first five observations 
data_tips.head()
#%% cell 
# this function should return a tuple of 3 values: the class of your dataset object, the shape of the dataset and 
#the columns names
def answer_3():
    # write your code here:
    # the type of the object data_tips 
    dataset_type=type(data_tips)
    # the shape of data 
    shape=data_tips.shape
    #variables in data
    col_names=data_tips.columns
   
    return dataset_type,shape,col_names
    
print (answer_3())

#%% cell 
#This function should return a dataframe including the new variable tip_rate
def answer_4():
    # write your code here
    data_tips['tip_rate']=data_tips['TIP']/data_tips['BILL']

    return data_tips
print (answer_4().tail())
#%% cell 
#This function should return summary about numerical and categorical features
# use the output of answer4() for your this question
def answer_5():
    
    s = pd.Categorical(answer_4().DAY, categories=[3,4,5,6])
    s.rename_categories(["Thu", "Fri", "Sat", "Sun"], inplace=True)
    answer_4()["CAT_DAY"] = s
    answer_4()["CAT_DAY"].astype('category')
    
    s = pd.Categorical(answer_4().TIME, categories=[0,1])
    s.rename_categories(["Day", "Night"], inplace=True)
    answer_4()["CAT_TIME"] = s
    answer_4()["CAT_TIME"].astype('category')
    
    s = pd.Categorical(answer_4().SMOKER, categories=[0,1])
    s.rename_categories(["No","Yes"], inplace=True)
    answer_4()["CAT_SMOKER"] = s
    answer_4()["CAT_SMOKER"].astype('category')
    
    s = pd.Categorical(answer_4().SEX, categories=[0,1]) ## define a categorical variable, 
    s.rename_categories(["M","F"], inplace=True) #inplace : boolean (default: False) Whether or not to rename the categories inplace or return a copy of this categorical with renamed categories.
    answer_4()["CAT_SEX"] = s
    answer_4()["CAT_SEX"].astype('category')
    
    # write your code here:
    num_des=answer_4().describe()
    cate_des=answer_4().describe(include="category")
    
    return num_des,cate_des
print (answer_5())

#%% cell 
# this function should return a plot of the days distribution, give a comment below your plot
def answer_6():
    # write your code here
    return sns.countplot(x='CAT_DAY',data=data_tips)
print (answer_6())

#%% cell 
# this function should return a plot of tips against the total_bill
def answer_7(): 
    # write your code here
    ax = sns.regplot(x="BILL", y="TIP", data=data_tips)
    print (data_tips)
    return ax
print (answer_7())  

#%% cell 
# these lines of code tests the correlation between our two variables: total_bill and tip
from scipy.stats import pearsonr,spearmanr
pearsonr(data_tips['TIP'],data_tips['BILL'])


# seconde way to test correlation using spearmanr test. The difference between spearmanr and pearsonr test is that spearmanr can
# be used for ordinal features also. Visit the link given above for more info.
spearmanr(data_tips['TIP'],data_tips['BILL'])

def answer_8():
    # write your code here
    plt.figure()
    boxplot_total_bill = sns.boxplot(x= 'BILL',data=data_tips,orient='v', whis=2)
    plt.figure()
    boxplot_tip =sns.boxplot(x= 'TIP',data=data_tips,orient='v')
    plt.figure()
    boxplot_tip_vs_day = sns.boxplot(x= 'CAT_DAY',y='TIP',data=data_tips, orient='v')
    plt.figure()
    boxplot_tip_vs_day_per = sns.boxplot(x= 'CAT_DAY',y='tip_rate',data=data_tips, orient='v')
    return boxplot_total_bill,boxplot_tip,boxplot_tip_vs_day,boxplot_tip_vs_day_per

print (answer_8())
#%% cell 
def answer_9():
    # write your code here
    #plt.subplot(nrows=2,ncols=3)
    for i in range(6,16,2):
        plt.figure()
        plt.hist(x='TIP',data=data_tips,huebins=i)
        plt.axvline(data_tips['TIP'].mean(),color='red') # add the mean value of tip to our plots
        plt.title('histogram for bins='+str(i))
print (answer_9())

#%% cell 
def answer_11():
    # write your code here
    ax1=pd.crosstab(data_tips.CAT_SMOKER,data_tips.CAT_SEX).plot.barh(stacked=True)
    ax2=pd.crosstab(data_tips.CAT_DAY,data_tips.CAT_TIME).plot.barh(stacked=True)

    return ax1,ax2
print (answer_11())

#%% cell 
from statsmodels.graphics.mosaicplot import mosaic
def answer_12():
    ax=mosaic(data_tips,['CAT_DAY','CAT_SEX'])
    
    return ax 

print (answer_12())
# men pay mostly and  on Sunday

#%% cell 
#You can explore more nice plots  with the seaborn library: http://seaborn.pydata.org/tutorial/categorical.html

sns.factorplot(x="CAT_DAY", y="TIP", hue="CAT_SMOKER", data=data_tips)  # estimator is the mean among each day
plt.figure()
boxplot_tip_vs_day = sns.boxplot(x= 'CAT_DAY',y='TIP',data=data_tips, orient='v')
sns.factorplot(x="CAT_DAY", y="TIP", hue="CAT_SMOKER", data=data_tips, kind="bar")

sns.factorplot(x="CAT_DAY", y="BILL", hue="CAT_SEX", data=data_tips, kind="bar")

#First, import some libraries. We use statsmodels.api.OLS for the linear regression since it contains a much more detailed 
#report on the results of the fit than sklearn.linear_model.LinearRegression.
# visit for useful info about OLS : http://efavdb.com/interpret-linear-regression/
import statsmodels.formula.api as sm
#%% cell 
#this function should return a dataframe including the dummies for 'day','sex','smoker' and 'time'
def answer_13_0():
    # write your code here:
    data_tips=answer_4()
    res= pd.get_dummies(data_tips,columns=['DAY'])
    #result=res.ix[:, 'day_Fri':].astype('object')
    #result2=pd.concat([answer_13().ix[:,'total_bill':'tip_rate'],result],axis=1)
    return res
print (answer_13_0().head(3))
#%% cell 
def answer_13():
    # write your code here:
    data_tips=answer_4()
    res= pd.get_dummies(data_tips,columns=['DAY','SEX','SMOKER','TIME'])
    #result=res.ix[:, 'day_Fri':].astype('object')
    #result2=pd.concat([answer_13().ix[:,'total_bill':'tip_rate'],result],axis=1)
    return res
print (answer_13().tail(5))

# answer13() provides a dataframe where the new columns are considered as float which is not true, the following lines of codes
# will resolve the problem for you.
#from now use the dataframe 'data'.
#result=answer_13().ix[:, 'day_Fri':].astype('object')

result=answer_13_0().ix[:, 'DAY_3':].astype('object')
#data=pd.concat([answer_13().ix[:,'BILL':'tip_rate'],result],axis=1)
data=pd.concat([answer_13_0().ix[:,'BILL':'tip_rate'],result],axis=1)

data.dtypes
#%% cell 
# this function should fit a general model respecting the requirements and return a summary about that model
#( use :  your_model.summary())
def answer_14_0():
    #answer_13()
    model=sm.ols(formula="data.tip_rate~data.SEX + data.SMOKER +data.TIME + data['SIZE'] + data.DAY_3 + data.DAY_4 + data.DAY_5 + data.DAY_6",data=data).fit()
    return model.summary()
print (answer_14_0())

#%% cell 
def answer_14():
    #answer_13()
    model=sm.ols(formula="data.tip_rate~data.sex_Female +data.sex_Male+ data.smoker_No+data.smoker_Yes +data.time_Dinner+data.time_Lunch + data['size'] + data.day_Fri + data.day_Thur + data.day_Sun + data.day_Sat ",data=data).fit()
    return model.summary()
print (answer_14())
#%% cell 
def answer_15():
    #write your code here
    #data_tips=answer_13()
    model=sm.ols(formula="data.tip_rate~data['SIZE']",data=data).fit()    
    return model.summary()

print (answer_15())
#%% cell 
# this function is provided since there is no specific method for aicstatistic in python
# the source code was taken from : http://planspace.org/20150423-forward_selection_with_statsmodels/
import statsmodels.formula.api as smf

def forward_selected(data, response):
    """Linear model designed by forward selection.

    Parameters:
    -----------
    data : pandas DataFrame with all possible predictors and response

    response: string, name of response column in data

    Returns:
    --------
    model: an "optimal" fitted statsmodels linear model
           with an intercept
           selected by forward selection
           evaluated by adjusted R-squared
    """
    remaining = set(data.columns)
    remaining.remove(response)
    selected = []
    current_score, best_new_score = 0.0, 0.0
    while remaining and current_score == best_new_score:
        scores_with_candidates = []
        for candidate in remaining:
            formula = "{} ~ {} ".format(response,
                                           ' + '.join(selected + [candidate]))
            score = smf.ols(formula, data).fit().rsquared_adj
            scores_with_candidates.append((score, candidate))
        scores_with_candidates.sort()
        best_new_score, best_candidate = scores_with_candidates.pop()
        if current_score < best_new_score:
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_new_score
    formula = "{} ~ {} ".format(response,
                                   ' + '.join(selected))
    model = smf.ols(formula, data).fit()
    return model


data.head(1)

def answer_16():
    data_new=data.iloc[:,2:12]
    model = forward_selected(data_new, 'tip_rate')
    return  model.model.formula ,model.rsquared_adj
print (answer_16())
#%% cell 
def answer_17():
    # write your code here
    model=sm.ols(formula="data.tip_rate~data.BILL",data=data).fit()
    return model.summary()
print (answer_17())
#%% cell 
def answer_18_1():
    corr=spearmanr(data['SIZE'],data['BILL'])

    return corr
print (answer_18_1())
#%% cell 
def answer_18_2():
    model=sm.ols(formula="data.tip_rate~data.BILL+data['SIZE']",data=data).fit()
    return model.summary()

print (answer_18_2())
#%% cell 
def answer_18_3():
    model=sm.ols(formula="data.tip_rate~data.BILL+data['SIZE']+(data.BILL)*(data['SIZE'])",data=data).fit()
    
    return model.summary()
print (answer_18_3())


