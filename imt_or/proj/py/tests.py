import dist_heat
import helpers
import pprint as pp
import pandas 
import numpy
import math
from operator import itemgetter, attrgetter
import pylab as pl
import matplotlib.pyplot as plt
import time

# DATA
excel_file = 'smalldata.xlsx'
nodes_coord = helpers.read_excel_data(excel_file, 'NodesCord')
number_of_nodes = len(nodes_coord)
distance_matrix = helpers.distance_between_edges_matrix(nodes_coord, number_of_nodes)
DATA = {
  'c_rev': helpers.read_excel_data(excel_file, 'crev'),
  'c_om': helpers.read_excel_data(excel_file, 'com'),
  'c_heat': helpers.read_excel_data(excel_file, 'cheat'),
  'c_var': helpers.read_excel_data(excel_file, 'cvar'),
  'c_fix': helpers.read_excel_data(excel_file, 'cfix'),
  'p_umd': helpers.read_excel_data(excel_file, 'pumd'),
  'v_var': helpers.read_excel_data(excel_file, 'vvar'),
  'v_fix': helpers.read_excel_data(excel_file, 'vfix'),
  'T_flh': helpers.read_excel_data(excel_file, 'Tflh')[0][0],
  'Betta': helpers.read_excel_data(excel_file, 'Betta')[0][0],
  'Lamda': helpers.read_excel_data(excel_file, 'Gamma')[0][0],
  'Alpha': helpers.read_excel_data(excel_file, 'Alpha')[0][0],
  'edges_peak_demand': helpers.read_excel_data(excel_file, 'EdgesDemandPeak'),
  'edges_annual_demand': helpers.read_excel_data(excel_file, 'EdgesDemandAnnual'),
  'C_max': helpers.read_excel_data(excel_file, 'Cmax'),
  'Q_max': helpers.read_excel_data(excel_file, 'SourceMaxCap')[0][0],
  'source': helpers.read_excel_data(excel_file, 'SourceNum')[0][0] - 1,
  'distance': distance_matrix,
  'number_of_nodes': number_of_nodes
}


## CONTSTANTS
POPULATION_SIZE = 300
ITERATIONS = 12
MINIMUM_IMPROVEMENT_TOLERANCE = 0.02
MAX_STATIC_IMPROVEMENT = 5
CROSSOVER_SINGLE_POINT = 1
CROSSOVER_SECOND_POINT = 2
CROSSOVER_RAND_SINGLE_POINT = 3
MUTATION_ALLELE_FLIP = 1
MUTATION_INSERTION = 2
MUTATION_DISPLACEMENT = 3
MUTATION_INVERSMENT = 4
MUTATION_DISPLACED_INVERSION = 5
MUTATION_INVASIVE_ALLELE_FLIP = 6
MUTATION_RAND_DISPLACEMENT = 7
MUTATION_RAND_DISPLACED_INVERSION = 8
KNOWN_BEST_ANSWER_FOR_SMALL_DATA = 26038797
PROPOSED_CONFIG = {'elitism': 4, 'crossover': 43, 'mutation': 43, 'hybrid': 10 }


# try with percentages of elite, crossover, mutatuon, elitism
# try with different combinations of algorithms for mutation and crossover

# one try
""" results = dist_heat.genetic_algorithm_district_heating(DATA, 
  1, # iterations
  10, # population size
  PROPOSED_CONFIG, 
  CROSSOVER_SINGLE_POINT, 
  CROSSOVER_RAND_SINGLE_POINT, 
  MUTATION_RAND_DISPLACEMENT, 
  MUTATION_RAND_DISPLACEMENT)
pp.pprint(results) """

TRIES = 10

available_crossover_algorithms = [CROSSOVER_SINGLE_POINT, CROSSOVER_SECOND_POINT, CROSSOVER_RAND_SINGLE_POINT]
available_mutation_algorithms = [MUTATION_ALLELE_FLIP, MUTATION_INSERTION, MUTATION_DISPLACEMENT, MUTATION_INVERSMENT, MUTATION_DISPLACED_INVERSION, MUTATION_INVASIVE_ALLELE_FLIP, MUTATION_RAND_DISPLACEMENT, MUTATION_RAND_DISPLACED_INVERSION]

big_data = []

start = time.time()

for crossover_first in available_crossover_algorithms : 
  for crossover_second in available_crossover_algorithms :
    for mutation_first in available_mutation_algorithms :
      for mutation_second in available_mutation_algorithms : 
        for elite_percentage in range(10, 10 + 1 , 5) :
          for hybrid_percentage in range(10, 10 + 1, 5) : 
            remaining_percentage = 100 - elite_percentage - hybrid_percentage
            # first configuration
            crossover_percentage = math.floor(remaining_percentage / 3)
            mutation_percentage = remaining_percentage - crossover_percentage
            configuration =  {'elitism': elite_percentage, 'crossover': crossover_percentage, 'mutation': mutation_percentage, 'hybrid': hybrid_percentage }
            results = dist_heat.genetic_algorithm_district_heating(DATA, ITERATIONS, POPULATION_SIZE, configuration, crossover_first, crossover_second, mutation_first, mutation_second)
            big_data.append(
              {
                'crossover': crossover_percentage, 
                'mutation': mutation_percentage,
                'crossover_1': crossover_first,
                'crossover_2': crossover_second,
                'mutation_1': mutation_first, 
                'mutation_2': mutation_second,
                'elitism': elite_percentage,
                'hybrid': hybrid_percentage,
                'best': results['best'][len(results['best']) - 1 ], 
                'duration': results['duration'], 
                'evaluation': results['best'][len(results['best']) - 1]['evaluation']
              })
            print('crossover (' + str(crossover_first) + ', ' + str(crossover_second) + ') : ' + str(crossover_percentage) + '%, mutation (' + str(mutation_first) + ', ' + str(mutation_second) + ') : ' + str(mutation_percentage) + '%, elite: ' + str(elite_percentage) + '%, hybrid: ' + str(hybrid_percentage) + '%, evaluation : ' + str(results['best'][len(results['best']) - 1]['evaluation']))
            #second
            crossover_percentage = math.floor(remaining_percentage / 2)
            mutation_percentage = remaining_percentage - crossover_percentage
            configuration =  {'elitism': elite_percentage, 'crossover': crossover_percentage, 'mutation': mutation_percentage, 'hybrid': hybrid_percentage }
            results = dist_heat.genetic_algorithm_district_heating(DATA, ITERATIONS, POPULATION_SIZE, configuration, crossover_first, crossover_second, mutation_first, mutation_second)
            big_data.append(
              {
                'crossover': crossover_percentage, 
                'mutation': mutation_percentage,
                'crossover_1': crossover_first,
                'crossover_2': crossover_second,
                'mutation_1': mutation_first, 
                'mutation_2': mutation_second,
                'elitism': elite_percentage,
                'hybrid': hybrid_percentage,
                'best': results['best'][len(results['best']) - 1 ], 
                'duration': results['duration'], 
                'evaluation': results['best'][len(results['best']) - 1]['evaluation']
              })
            print('crossover (' + str(crossover_first) + ', ' + str(crossover_second) + ') : ' + str(crossover_percentage) + '%, mutation (' + str(mutation_first) + ', ' + str(mutation_second) + ') : ' + str(mutation_percentage) + '%, elite: ' + str(elite_percentage) + '%, hybrid: ' + str(hybrid_percentage) + '%, evaluation : ' + str(results['best'][len(results['best']) - 1]['evaluation']))
            #third
            mutation_percentage = math.floor(remaining_percentage / 3)
            crossover_percentage = remaining_percentage - mutation_percentage
            configuration =  {'elitism': elite_percentage, 'crossover': crossover_percentage, 'mutation': mutation_percentage, 'hybrid': hybrid_percentage }
            results = dist_heat.genetic_algorithm_district_heating(DATA, ITERATIONS, POPULATION_SIZE, configuration, crossover_first, crossover_second, mutation_first, mutation_second)
            big_data.append(
              {
                'crossover': crossover_percentage, 
                'mutation': mutation_percentage,
                'crossover_1': crossover_first,
                'crossover_2': crossover_second,
                'mutation_1': mutation_first, 
                'mutation_2': mutation_second,
                'elitism': elite_percentage,
                'hybrid': hybrid_percentage,
                'best': results['best'][len(results['best']) - 1 ], 
                'duration': results['duration'], 
                'evaluation': results['best'][len(results['best']) - 1]['evaluation']
              })
            print('crossover (' + str(crossover_first) + ', ' + str(crossover_second) + ') : ' + str(crossover_percentage) + '%, mutation (' + str(mutation_first) + ', ' + str(mutation_second) + ') : ' + str(mutation_percentage) + '%, elite: ' + str(elite_percentage) + '%, hybrid: ' + str(hybrid_percentage) + '%, evaluation : ' + str(results['best'][len(results['best']) - 1]['evaluation']))

end = time.time()
print('duration: ' + str(end - start))

sorted_big_data = sorted(big_data, key=itemgetter('evaluation'))

series_big_data = pandas.Series(sorted_big_data)
data_frame_big_data = pandas.DataFrame(sorted_big_data, index=series_big_data.index, columns=['evaluation', 'hybrid', 'mutation', 'elitism', 'crossover', 'crossover_1', 'crossover_2', 'mutation_1', 'mutation_2'])

data_frame_big_data.to_pickle('data/genetic_study.pkl')

data_frame_big_data.plot.scatter(x='evaluation', y='crossover')
plt.savefig('figures/scatter-eval-cross'+'.pdf', dpi=100)
data_frame_big_data.plot.scatter(x='evaluation', y='mutation')
plt.savefig('figures/scatter-eval-mut'+'.pdf', dpi=100)
data_frame_big_data.plot.scatter(x='evaluation', y='hybrid')
plt.savefig('figures/scatter-eval-hy'+'.pdf', dpi=100)
data_frame_big_data.plot.scatter(x='evaluation', y='elitism')
plt.savefig('figures/scatter-eval-elit'+'.pdf', dpi=100)

#best 20
for n in range(20) :
  pp.pprint(sorted_big_data[n])

