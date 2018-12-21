### TEST ENVIRONNMENT
import helpers
import tests
import math
import time

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
POPULATION_SIZE = math.ceil(number_of_nodes**2 * (4/3) * math.log(number_of_nodes) / 10) * 10
ITERATIONS = 6 * math.floor(math.log(number_of_nodes))
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
TRIES = 10
chosen_crossover_algorithms = [CROSSOVER_RAND_TWO_POINT, CROSSOVER_UNIFORM] 
chosen_mutation_algorithms = [MUTATION_INVERSION, MUTATION_ALLELE_FLIP]
print('population_size = ' + str(POPULATION_SIZE))
tests.run_GA(
  TRIES, 
  DATA, 
  chosen_crossover_algorithms[0], 
  chosen_crossover_algorithms[1], 
  chosen_mutation_algorithms[0], 
  chosen_mutation_algorithms[1], 
  ITERATIONS, 
  POPULATION_SIZE, 
  0, # HYBRID_OUTSIDE 0 -> FALSE [1 - 100]%
  PROPOSED_CONFIG, 
  'data_GA',
  str(time.time()) + '_genetic')