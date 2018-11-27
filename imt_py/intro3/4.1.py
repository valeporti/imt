import pandas as pd
from pylab import *

pieces = []
columns = ['name', 'sex', 'births']
years = range(1880, 2011)
for year in years:
  path = './names/yob%d.txt' % year
  frame = pd.read_csv(path, names=columns)
  frame['year'] = year
  pieces.append(frame)
names = pd.concat(pieces, ignore_index=True)

total_births = names.pivot_table(values='births', index='year', columns=['sex'], aggfunc=sum)
total_births.plot(title='Total of births by year and by sex')
# show()

def add_prop(group):
  births = group.births.astype(float)
  group['prop'] = births / births.sum()
  return group

names = names.groupby(['year','sex']).apply(add_prop)

def get_top1000(group):
  return group.sort_values(by='births',ascending=False)[:1000]

grouped = names.groupby(['year','sex'])
top1000 = grouped.apply(get_top1000)

total_births = top1000.pivot_table('births', index='year', columns='name', aggfunc=sum)

subset = total_births[['John','Harry','Mary','Marilyn']]
subset.plot(subplots=True, figsize=(12,10), grid=False, title='Total births per year')
show()

table = top1000.pivot_table('prop',index='year',columns='sex',aggfunc=sum)
table.plot(title='Sum of frequencies per year and sex',yticks=np.linspace(0,1.2,13),xticks=range(1880,2020,10))
show()

# Diversity  of first names
boys = top1000[top1000.sex == 'M']
df = boys[boys.year == 2010]
prop_cumsum = df.sort_values(by='prop',ascending=False).prop.cumsum()

