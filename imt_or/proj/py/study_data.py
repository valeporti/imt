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

FILE_5 = 'data/err_ga_st_hyout_hyin.pkl'
FILE_5_SUB = 'figures/err_ga_st_hyout_hyin/' #opt_hybrid_out_in

## FROM HERE!!!! (BEFORE ERRORS)
FILE_6 = 'data/ga_st_NOhybrids_methods_study.pkl'
FILE_6_SUB = 'figures/ga_st_NOhybrids_methods_study/' #opt_test_methods_0hybrid
# best configuration CO [2,3]
# best configuration M [1,1], [4,1], []
FILE_7 = 'data/ga_st_hyout_hyin_hynone.pkl'
FILE_7_SUB = 'figures/ga_st_hyout_hyin_hynone/' #opt_hybrid_out_in_none
FILE_8 = 'data/err_study_various_repetitions.pkl'
FILE_8_SUB = 'figures/err_study_various_repetitions/'#study_various_repetitions
FILE_9 = 'data/opt_study_various_repetitions.pkl'
FILE_9_SUB = 'figures/opt_study_various_repetitions/'
FILE_10 = 'data/ga_st_repeat_conf_300_smalldata.pkl'
FILE_10_SUB = 'figures/ga_st_repeat_conf_300_smalldata/' #opt_duration_study_various_repetitions

FILE_11 = 'data/ga_st_repeat_conf_50_largedata.pkl'
FILE_11_SUB = 'figures/ga_st_repeat_conf_50_largedata/' #opt_study_50_large

FILE_12 = 'data/ga_st_repeat_conf_20_smalldata.pkl'
FILE_12_SUB = 'figures/ga_st_repeat_conf_20_smalldata/' #opt_pop_small_20try
#See if method has a lot of influence
FILE_13 = 'data/opt_pop_large_10try_invasiveflip.pkl'
FILE_13_SUB = 'figures/opt_pop_large_10try_invasiveflip/'

FILE_14 = 'data/ga_st_2000_pop_largedata.pkl'
FILE_14_SUB = 'figures/ga_st_2000_pop_largedata/' #opt_pop_large_10try
# populations small
FILE_15 = 'data/pop_100_small.pkl'
FILE_15_SUB = 'figures/pop_100_small/'
FILE_16 = 'data/pop_200_small.pkl'
FILE_16_SUB = 'figures/pop_200_small/'
FILE_17 = 'data/pop_300_small.pkl'
FILE_17_SUB = 'figures/pop_300_small/'
FILE_18 = 'data/pop_2050_large.pkl'
FILE_18_SUB = 'figures/pop_2050_large/'

figures_directory = FILE_9_SUB
data_directory = FILE_14

""" if not os.path.exists(figures_directory):
  os.makedirs(figures_directory) """

df = pandas.read_pickle(data_directory)

print(df.describe())


# STUDY VARIOUS REPETITIONS DIFFETENT POPULATION
# for small data
""" df1 = pandas.read_pickle(FILE_15)
df2 = pandas.read_pickle(FILE_16)
df3 = pandas.read_pickle(FILE_17)
print(df3.describe()) """
# for large data
""" df1 = pandas.read_pickle(FILE_14)
df2 = pandas.read_pickle(FILE_11)
df3 = pandas.read_pickle(FILE_18)
frames = [df1, df2, df3]
df = pandas.concat(frames)
df.boxplot(column='evaluation', by=['population'])
plt.savefig(figures_directory + 'boxplot_pop_small.eps', dpi=100)
pprint.pprint(df3['best'][0])
print(df3.describe  """

#%%cell
# STUDY VARIOUS REPETITIONS SAME CONFIGURATION
""" df.boxplot(column='evaluation')
plt.savefig(figures_directory + 'boxplot_small.eps', dpi=100)
print(df)
print(df.describe()) """

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