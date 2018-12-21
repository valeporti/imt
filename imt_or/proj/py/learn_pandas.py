import pandas 
import numpy
import pprint
import pylab as pl
import os
import matplotlib.pyplot as plt

big_data = [
{'best': {'evaluation': 26038796.98501206,
          'flow': {'flow_tree': {0: {'child': [3], 'parent': 1},
                                 1: {'child': [0], 'parent': 2},
                                 2: {'child': [1], 'parent': 4},
                                 3: {'child': [7], 'parent': 0},
                                 4: {'child': [5, 2], 'parent': -1},
                                 5: {'child': [6], 'parent': 4},
                                 6: {'child': [], 'parent': 5},
                                 7: {'child': [], 'parent': 3}},
                   'leaves': [6, 7],
                   'root': 4},
          'prufer': [5, 4, 2, 1, 0, 3],
          'tree': [(5, 6), (4, 5), (2, 4), (1, 2), (0, 1), (3, 0), (3, 7)]},
 'crossover': 28,
 'duration': 0.0018649101257324219,
 'elitism': 10,
 'evaluation': 26038796.98501206,
 'hybrid': 5,
 'mutation': 57},
{'best': {'evaluation': 26038796.98501206,
          'flow': {'flow_tree': {0: {'child': [3], 'parent': 1},
                                 1: {'child': [0], 'parent': 2},
                                 2: {'child': [1], 'parent': 4},
                                 3: {'child': [7], 'parent': 0},
                                 4: {'child': [5, 2], 'parent': -1},
                                 5: {'child': [6], 'parent': 4},
                                 6: {'child': [], 'parent': 5},
                                 7: {'child': [], 'parent': 3}},
                   'leaves': [6, 7],
                   'root': 4},
          'prufer': [5, 4, 2, 1, 0, 3],
          'tree': [(5, 6), (4, 5), (2, 4), (1, 2), (0, 1), (3, 0), (3, 7)]},
 'crossover': 50,
 'duration': 0.004967451095581055,
 'elitism': 10,
 'evaluation': 26038796.98501206,
 'hybrid': 15,
 'mutation': 25},
{'best': {'evaluation': 26718562.606059276,
          'flow': {'flow_tree': {0: {'child': [], 'parent': 3},
                                 1: {'child': [], 'parent': 2},
                                 2: {'child': [1], 'parent': 4},
                                 3: {'child': [0], 'parent': 7},
                                 4: {'child': [2, 5], 'parent': -1},
                                 5: {'child': [6], 'parent': 4},
                                 6: {'child': [7], 'parent': 5},
                                 7: {'child': [3], 'parent': 6}},
                   'leaves': [1, 0],
                   'root': 4},
          'prufer': [3, 2, 4, 7, 5, 6],
          'tree': [(3, 0), (2, 1), (4, 2), (7, 3), (5, 4), (6, 5), (6, 7)]},
 'crossover': 60,
 'duration': 0.004945039749145508,
 'elitism': 0,
 'evaluation': 26718562.606059276,
 'hybrid': 10,
 'mutation': 30},
{'best': {'evaluation': 26740904.89979841,
          'flow': {'flow_tree': {0: {'child': [1], 'parent': 3},
                                 1: {'child': [], 'parent': 0},
                                 2: {'child': [], 'parent': 4},
                                 3: {'child': [0], 'parent': 7},
                                 4: {'child': [2, 5], 'parent': -1},
                                 5: {'child': [6], 'parent': 4},
                                 6: {'child': [7], 'parent': 5},
                                 7: {'child': [3], 'parent': 6}},
                   'leaves': [2, 1],
                   'root': 4},
          'prufer': [0, 3, 4, 7, 5, 6],
          'tree': [(0, 1), (3, 0), (4, 2), (7, 3), (5, 4), (6, 5), (6, 7)]},
 'crossover': 60,
 'duration': 0.0028781890869140625,
 'elitism': 5,
 'evaluation': 26740904.89979841,
 'hybrid': 5,
 'mutation': 30},
{'best': {'evaluation': 26894186.52914352,
          'flow': {'flow_tree': {0: {'child': [], 'parent': 3},
                                 1: {'child': [3], 'parent': 2},
                                 2: {'child': [1], 'parent': 4},
                                 3: {'child': [0], 'parent': 1},
                                 4: {'child': [2, 5], 'parent': -1},
                                 5: {'child': [6], 'parent': 4},
                                 6: {'child': [7], 'parent': 5},
                                 7: {'child': [], 'parent': 6}},
                   'leaves': [0, 7],
                   'root': 4},
          'prufer': [3, 1, 2, 4, 5, 6],
          'tree': [(3, 0), (1, 3), (2, 1), (4, 2), (5, 4), (6, 5), (6, 7)]},
 'crossover': 64,
 'duration': 0.001865386962890625,
 'elitism': 0,
 'evaluation': 26894186.52914352,
 'hybrid': 5,
 'mutation': 31},
{'best': {'evaluation': 26909875.25067108,
          'flow': {'flow_tree': {0: {'child': [], 'parent': 1},
                                 1: {'child': [0, 3], 'parent': 2},
                                 2: {'child': [1], 'parent': 4},
                                 3: {'child': [], 'parent': 1},
                                 4: {'child': [2, 5], 'parent': -1},
                                 5: {'child': [6], 'parent': 4},
                                 6: {'child': [7], 'parent': 5},
                                 7: {'child': [], 'parent': 6}},
                   'leaves': [0, 3, 7],
                   'root': 4},
          'prufer': [1, 1, 2, 4, 5, 6],
          'tree': [(1, 0), (1, 3), (2, 1), (4, 2), (5, 4), (6, 5), (6, 7)]},
 'crossover': 30,
 'duration': 0.005075216293334961,
 'elitism': 0,
 'evaluation': 26909875.25067108,
 'hybrid': 10,
 'mutation': 60},
{'best': {'evaluation': 27019323.924925167,
          'flow': {'flow_tree': {0: {'child': [1], 'parent': 3},
                                 1: {'child': [2], 'parent': 0},
                                 2: {'child': [], 'parent': 1},
                                 3: {'child': [0], 'parent': 7},
                                 4: {'child': [5], 'parent': -1},
                                 5: {'child': [6], 'parent': 4},
                                 6: {'child': [7], 'parent': 5},
                                 7: {'child': [3], 'parent': 6}},
                   'leaves': [2],
                   'root': 4},
          'prufer': [1, 0, 3, 7, 5, 6],
          'tree': [(1, 2), (0, 1), (3, 0), (7, 3), (5, 4), (6, 5), (6, 7)]},
 'crossover': 25,
 'duration': 0.008513689041137695,
 'elitism': 5,
 'evaluation': 27019323.924925167,
 'hybrid': 20,
 'mutation': 50},
{'best': {'evaluation': 27124448.310554918,
          'flow': {'flow_tree': {0: {'child': [], 'parent': 3},
                                 1: {'child': [], 'parent': 3},
                                 2: {'child': [], 'parent': 4},
                                 3: {'child': [0, 1], 'parent': 7},
                                 4: {'child': [2, 5], 'parent': -1},
                                 5: {'child': [6], 'parent': 4},
                                 6: {'child': [7], 'parent': 5},
                                 7: {'child': [3], 'parent': 6}},
                   'leaves': [2, 0, 1],
                   'root': 4},
          'prufer': [3, 3, 4, 7, 5, 6],
          'tree': [(3, 0), (3, 1), (4, 2), (7, 3), (5, 4), (6, 5), (6, 7)]},
 'crossover': 42,
 'duration': 0.005117177963256836,
 'elitism': 0,
 'evaluation': 27124448.310554918,
 'hybrid': 15,
 'mutation': 43},
{'best': {'evaluation': 27176808.808828905,
          'flow': {'flow_tree': {0: {'child': [], 'parent': 1},
                                 1: {'child': [0], 'parent': 3},
                                 2: {'child': [], 'parent': 4},
                                 3: {'child': [1], 'parent': 7},
                                 4: {'child': [2, 5], 'parent': -1},
                                 5: {'child': [6], 'parent': 4},
                                 6: {'child': [7], 'parent': 5},
                                 7: {'child': [3], 'parent': 6}},
                   'leaves': [2, 0],
                   'root': 4},
          'prufer': [1, 3, 4, 7, 5, 6],
          'tree': [(1, 0), (3, 1), (4, 2), (7, 3), (5, 4), (6, 5), (6, 7)]},
 'crossover': 26,
 'duration': 0.012164592742919922,
 'elitism': 0,
 'evaluation': 27176808.808828905,
 'hybrid': 20,
 'mutation': 54},
{'best': {'evaluation': 27306236.345883254,
          'flow': {'flow_tree': {0: {'child': [], 'parent': 3},
                                 1: {'child': [3], 'parent': 2},
                                 2: {'child': [1], 'parent': 4},
                                 3: {'child': [0, 7], 'parent': 1},
                                 4: {'child': [5, 2], 'parent': -1},
                                 5: {'child': [], 'parent': 4},
                                 6: {'child': [], 'parent': 7},
                                 7: {'child': [6], 'parent': 3}},
                   'leaves': [5, 0, 6],
                   'root': 4},
          'prufer': [3, 4, 2, 1, 3, 7],
          'tree': [(3, 0), (4, 5), (2, 4), (1, 2), (3, 1), (7, 3), (6, 7)]},
 'crossover': 40,
 'duration': 0.004991054534912109,
 'elitism': 5,
 'evaluation': 27306236.345883254,
 'hybrid': 15,
 'mutation': 40},
]


series_big_data = pandas.Series(big_data)

data_frame_big_data = pandas.DataFrame(big_data, index=series_big_data.index, columns=['evaluation', 'hybrid', 'mutation', 'elitism', 'crossover'])


data_frame_big_data.plot.scatter(x='evaluation', y='crossover')
plt.savefig('figures/scatter-eval-cross'+'.pdf', dpi=100)
data_frame_big_data.plot.scatter(x='evaluation', y='mutation')
plt.savefig('figures/scatter-eval-mut'+'.pdf', dpi=100)
data_frame_big_data.plot.scatter(x='evaluation', y='hybrid')
plt.savefig('figures/scatter-eval-hy'+'.pdf', dpi=100)
data_frame_big_data.plot.scatter(x='evaluation', y='elitism')
plt.savefig('figures/scatter-eval-elit'+'.pdf', dpi=100)

data_frame_big_data.to_pickle('data/genetic_study.pkl')

new_data = pandas.read_pickle('data/proposed_study.pkl')
print(new_data)
