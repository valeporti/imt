### TEST ENVIRONNMENT
import helpers
import tests
import math
import time

## CONTSTANTS
MINIMUM_IMPROVEMENT_TOLERANCE = 0.02
MAX_STATIC_IMPROVEMENT = 5
CROSSOVER_RAND_SINGLE_POINT = 1
CROSSOVER_RAND_TWO_POINT = 2
CROSSOVER_UNIFORM = 3
MUTATION_ALLELE_FLIP = 1
MUTATION_INSERTION = 2
MUTATION_DISPLACEMENT = 3 
MUTATION_INVERSION = 4
MUTATION_DISPLACED_INVERSION = 5 
MUTATION_INVASIVE_ALLELE_FLIP = 6
MUTATION_RAND_DISPLACEMENT = 7
MUTATION_RAND_DISPLACED_INVERSION = 8
KNOWN_BEST_ANSWER_FOR_SMALL_DATA = 26038797
PROPOSED_CONFIG = {'elitism': 10, 'crossover': 52, 'mutation': 28, 'hybrid': 10 }

# Run selected configuration
TRIES = 20
chosen_crossover_algorithms = [CROSSOVER_RAND_TWO_POINT, CROSSOVER_UNIFORM] 
chosen_mutation_algorithms = [MUTATION_INVERSION, MUTATION_ALLELE_FLIP]
DATA = helpers.get_data('smalldata.xlsx')
POPULATION_SIZE = math.ceil(DATA['number_of_nodes'] * (4/3) * math.log((3/2) * DATA['number_of_nodes']**2)**2 / 10) * 10
ITERATIONS = 4 + DATA['number_of_nodes']
print('population_size = ' + str(POPULATION_SIZE))
tests.run_GA(
  TRIES, # Number of runs
  DATA, # make sure you're loading correct file
  chosen_crossover_algorithms[0], 
  chosen_crossover_algorithms[1], 
  chosen_mutation_algorithms[0], 
  chosen_mutation_algorithms[1], 
  ITERATIONS, 
  POPULATION_SIZE, 
  0, # HYBRID_OUTSIDE 0 -> FALSE [1 - 100]%
  PROPOSED_CONFIG, 
  'data', # directory to use in order to save obtained results
  str(time.time()) + '_genetic') # name of the file