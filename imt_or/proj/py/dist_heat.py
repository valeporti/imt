import helpers
import evaluation
import crossover
import selection
import mutation
import math
import pprint as pp
from operator import itemgetter, attrgetter
import random

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
  'source': helpers.read_excel_data(excel_file, 'SourceNum')[0][0],
  'distance': distance_matrix,
  'number_of_nodes': number_of_nodes
}


## GA Algorithm Implementation
POPULATION_SIZE = 100
ITERATIONS = 20
MINIMUM_IMPROVEMENT_TOLERANCE = 0.05
best_solutions = []
proposed_config = {'elitism': 10, 'crossover': 70, 'mutation': 20 }
tolerance_best  = 0
best_solutions_opt_counter = 0

# POPULATION INITIALIZATION
population = helpers.get_tree_based_population(POPULATION_SIZE, DATA['number_of_nodes'], DATA['source'])

for i in range(ITERATIONS):

  from_individual = 0
  new_population = []
  
  # EVALUATION OF INDIVUDUALS IN POPULATION
  helpers.generate_tree_flow(population, DATA['source'])
  sum_evalutation = evaluation.evaluate(population, DATA)

  # SELECTION
  sorted_population = sorted(population, key=itemgetter('evaluation'))
  best_solutions.append(sorted_population[0])
  probabilities = selection.get_probability_list(sum_evalutation, sorted_population)

  from_individual = math.floor(proposed_config['elitism'] * POPULATION_SIZE / 100)
  new_population = sorted_population[:from_individual]

  # CROSSOVER
  for i in range(from_individual, from_individual + math.floor(POPULATION_SIZE * (proposed_config['crossover'])/ 100), 2) :
    index_parent_1 = selection.select_roulette(POPULATION_SIZE, probabilities)
    index_parent_2 = selection.select_roulette(POPULATION_SIZE, probabilities)
    children = crossover.crossover(0, sorted_population[index_parent_1]['prufer'], sorted_population[index_parent_2]['prufer'], DATA['number_of_nodes'] - 2)

    new_population.append(helpers.create_new_individual())
    new_population.append(helpers.create_new_individual())
    new_population[i]['prufer'] = children[0]
    new_population[i+1]['prufer'] = children[1]
    
  # MUTATION
  from_individual += math.floor(POPULATION_SIZE * (proposed_config['crossover'])/ 100)
  for i in range(from_individual, from_individual + math.floor(POPULATION_SIZE * (proposed_config['mutation'])/ 100)) :
    index_chromosome = selection.select_roulette(POPULATION_SIZE, probabilities)
    chromosome = mutation.mutation(1, sorted_population[index_chromosome]['prufer'], DATA['number_of_nodes'] - 2)
    new_population.append(helpers.create_new_individual())
    new_population[i]['prufer'] = chromosome

  # HYBRID PROPOSAL

  # NEXT GENERATION
  population = new_population[:]

  # TERMINATION CRITERIA
  best_len = len(best_solutions)
  tolerance_best += abs(best_solutions[best_len - 2]['evaluation'] - best_solutions[best_len - 1]['evaluation']) / best_solutions[best_len - 1]['evaluation']
  print(tolerance_best)
  if (best_solutions[best_len - 1]['evaluation'] == best_solutions[best_len - 2]['evaluation'] or tolerance_best < MINIMUM_IMPROVEMENT_TOLERANCE) :
    best_solutions_opt_counter += 1
  else :
    best_solutions_opt_counter = 0
  
  if best_solutions_opt_counter == 10 : break

pp.pprint(best_solutions)


#for n in range(POPULATION_SIZE):
#  pp.pprint(sorted_population[n]['evaluation'])

#  print(probabilities)
#  print(len(probabilities))
#  count = [0]*POPULATION_SIZE
#  for i in range(1000) : 
#    rand = random.uniform(0,probabilities[0])
#    for j in range (POPULATION_SIZE) :
#      if (j + 1 < POPULATION_SIZE and rand > probabilities[j + 1]) :
#        count[j] += 1
#        break
#      if (j + 1 == POPULATION_SIZE):
#        count[j] += 1
#  print(count)     
#  print(sum(count))



#print(population[0])
#print(population)
#population[0]['tree'] = helpers.prufer_to_tree(population[0]['prufer'])
#print(population[0]['tree'])
#arr1 = [1, 2, 3, 4, 5, 6]
#arr2 = [8, 9, 10, 11, 12, 13]

#let = cm.single_point_CO(arr1, arr2, len(arr1), math.floor((7)/2) )
#print(let)
#let2 = cm.second_point_CO(arr1, arr2, len(arr1))
#print(let2)
#let3 = cm.allele_flip_M(let2[0], len(arr1))
#print(let2[0])

#arr3 = [1, 2,3, 4, 5]
#cm.insertion_M(arr3, len(arr3))
#print(arr3)

#prufer_Of_individual = helpers.prufer_to_tree(population[0]['prufer']
#population[0]['tree'] = helpers.prufer_to_tree(population[0]['prufer'])
#print(population[0])
#for n in helpers.prufer_to_tree(population[0]['tree']: