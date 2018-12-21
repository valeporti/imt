import pandas 
import numpy as np
import pprint
import pylab as pl
import os
import matplotlib.pyplot as plt

FILE_1 = 'data/genetic_study_fixed_rand_CO_M_dyn_config.pkl'
FILE_1_SUB = 'figures/fixed_CO_M_dyn_config/'
FILE_2 = 'data/genetic_study_dyn_test_methods.pkl'
FILE_2_SUB = 'figures/dyn_test_methods/'
FILE_3 = 'data/genetic_study_NOHybrid_dyn_CO_M.pkl'
FILE_3_SUB = 'figures/no_hybrid_dyn_CO_M/'
# best configuration CO [3,2]
# best configuration M [1,1], [6,1], []
FILE_4 = 'data/genetic_hybrid_study_out_in.pkl'
FILE_4_SUB = 'figures/hybrid_out_in/'
FILE_5 = 'data/opt_genetic_hybrid_study_out_in.pkl'
FILE_5_SUB = 'figures/opt_hybrid_out_in/'
FILE_6 = 'data/opt_genetic_study_test_methods_0hybrid.pkl'
FILE_6_SUB = 'figures/opt_test_methods_0hybrid/'
# best configuration CO [2,3]
# best configuration M [1,1], [4,1], []
FILE_7 = 'data/opt_genetic_hybrid_study_out_in_none.pkl'
FILE_7_SUB = 'figures/opt_hybrid_out_in_none/'
FILE_8 = 'data/study_various_repetitions.pkl'
FILE_8_SUB = 'figures/study_various_repetitions/'
FILE_9 = 'data/opt_study_various_repetitions.pkl'
FILE_9_SUB = 'figures/opt_study_various_repetitions/'
FILE_10 = 'data/opt_duration_study_various_repetitions.pkl'
FILE_10_SUB = 'figures/opt_duration_study_various_repetitions/'


figures_directory = FILE_9_SUB
data_directory = FILE_9

if not os.path.exists(figures_directory):
  os.makedirs(figures_directory)

df = pandas.read_pickle(data_directory)

#%%cell
# STUDY VARIOUS REPETITIONS SAME CONFIGURATION
df.boxplot(column='evaluation')
plt.savefig(figures_directory + 'boxplot_small.eps', dpi=100)
#print(df.describe())
#eval_col = df['evaluation']
#print(eval_col.describe())
#print(eval_col.describe()['min'])
#df['count'] = df.groupby('evaluation').value()
#print(df)


grouped = df.groupby(['evaluation']).size()

print(grouped)
print(df['evaluation'].min())
plt.figure()
print(grouped.values)
""" grouped.hist()
plt.savefig(figures_directory + 'histrogram.eps', dpi=100) """
grouped.plot.scatter(x='evaluation', y='hybrid')
plt.figure()
plt.savefig(figures_directory + 'scatter.pdf', dpi=100)


""" frequency = np.array(df['evaluation'].value_counts())
freq_vals = np.array(frequency.index.tolist())
freq_index = range(len(frequency))
freq_s = pandas.Series(freq_vals, index=freq_index)

#freq_df = pandas.DataFrame(data=[np.array(freq_vals), np.array(frequency.values)], index=freq_index, columns=['evaluation', 'count'])

#frequency.hist(range=None, normed=False, weights=None)
#plt.savefig(figures_directory + 'histrogram.eps', dpi=100)
#x = frequency[0] """



#%%cell
# STUDY HYBRID

""" df.boxplot(column='evaluation', by=['hybrid', 'hybrid_outside'])
plt.savefig(figures_directory + 'boxplot_hybrid.eps', dpi=100) """

#%%cell
# STUDY CROSSOVER FILES 1-3
# Crossover Methods
""" crossover_methods = df.pivot_table(index = 'crossover_1', columns = 'crossover_2', values = 'evaluation', aggfunc=np.average)

group_cross = df['evaluation'].groupby([df['crossover_1'], df['crossover_2']])
group_cross.agg([len, np.sum, np.mean, np.std, np.max])
df.boxplot(column='evaluation', by=['crossover_1', 'crossover_2'])
plt.savefig(figures_directory + 'boxplot_cross_comb.eps', dpi=100)
df.boxplot(column='evaluation', by=['crossover_1'])
plt.savefig(figures_directory + 'boxplot_cross_1.eps', dpi=100)
df.boxplot(column='evaluation', by=['crossover_2'])
plt.savefig(figures_directory + 'boxplot_cross_2.eps', dpi=100)

# Mutation Methods
mutation_methods = df.pivot_table(index = 'mutation_1', columns = 'mutation_2', values = 'evaluation', aggfunc=np.average)

group_muta = df['evaluation'].groupby([df['mutation_1'], df['mutation_2']])
group_muta.agg([len, np.sum, np.mean, np.std, np.max])
df.boxplot(column='evaluation', by=['mutation_1', 'mutation_2'], rot=90, fontsize=5)
plt.savefig(figures_directory + 'boxplot_muta_comb.eps', dpi=100)
df.boxplot(column='evaluation', by=['mutation_1'], rot=90)
plt.savefig(figures_directory + 'boxplot_muta_1.eps', dpi=100)
df.boxplot(column='evaluation', by=['mutation_2'], rot=90)
plt.savefig(figures_directory + 'boxplot_muta_2.eps', dpi=100)

# Crossover and Mutation Percentages
df.boxplot(column='evaluation', by=['mutation', 'crossover'])
plt.savefig(figures_directory + 'boxplot_muta_cross_config.eps', dpi=100) """