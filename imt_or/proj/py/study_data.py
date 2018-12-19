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
FILE_7_SUB = 'figures/opt_hybrid_out_in_none'

figures_directory = FILE_7_SUB
data_directory = FILE_7

if not os.path.exists(figures_directory):
  os.makedirs(figures_directory)

df = pandas.read_pickle(data_directory)

#%%cell
# STUDY HYBRID
print(df)
df.boxplot(column='evaluation', by=['hybrid', 'hybrid_outside'])
plt.savefig(figures_directory + 'boxplot_hybrid.eps', dpi=100)

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