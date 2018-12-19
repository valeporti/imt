import helpers
import evaluation
import crossover
import selection
import mutation
import mutation_Raymond
import math
import time
import hybrid
import pprint as pp
from operator import itemgetter, attrgetter
import random

""" # DATA
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
} """


## CONTSTANTS
POPULATION_SIZE = 1
ITERATIONS = 1
MINIMUM_IMPROVEMENT_TOLERANCE = 0.02
MAX_STATIC_IMPROVEMENT = 7
CROSSOVER_RAND_SINGLE_POINT = 1
CROSSOVER_RAND_TWO_POINT = 2
CROSSOVER_UNIFORM = 3
CROSSOVER_SINGLE_POINT = 4
CROSSOVER_TWO_POINT = 5
CROSSOVER_UNIFORM = 3
MUTATION_ALLELE_FLIP_OPT = 1
MUTATION_INSERTION_OPT = 2
MUTATION_DISPLACEMENT_OPT = 3
MUTATION_INVERSMENT_OPT = 4
MUTATION_DISPLACED_INVERSION_OPT = 5
MUTATION_INVASIVE_ALLELE_FLIP_OPT = 6
MUTATION_RAND_DISPLACEMENT = 7
MUTATION_RAND_DISPLACED_INVERSION = 8
KNOWN_BEST_ANSWER_FOR_SMALL_DATA = 26038797

PROPOSED_CONFIG = {'elitism': 4, 'crossover': 43, 'mutation': 43, 'hybrid': 10 }

## GA Algorithm Implementation
def genetic_algorithm_district_heating (DATA, iterations, population_size, hybrid_outside, proposed_config = PROPOSED_CONFIG, first_CO = CROSSOVER_RAND_TWO_POINT, second_CO = CROSSOVER_RAND_TWO_POINT, first_M = MUTATION_INVASIVE_ALLELE_FLIP_OPT, second_M = MUTATION_DISPLACED_INVERSION_OPT) :

  start = time.time()
  best_solutions = []
  best_solutions_opt_counter = 0

  # POPULATION INITIALIZATION
  population = helpers.get_tree_based_population(population_size, DATA['number_of_nodes'], DATA['source'])
  sorted_population = []
  probabilities = []

  for it in range(iterations):

    """ arr1 = [1, 2, 3, 4, 5, 6]
    arr2 = [8, 9, 10, 11, 12, 13]
    
    arr_new = mutation.mutation(7, arr1, len(arr1))
    arr_new2 = mutation.mutation(3, arr1, len(arr1))
    print('arr1.: ')
    print(arr_new)
    print(arr_new2)
    children = crossover.crossover(5, arr1, arr2, len(arr1))
    print(children) """

    from_individual = 0
    total_done = 0
    new_population = []
    
    # EVALUATION OF INDIVUDUALS IN POPULATION
    sum_evalutation = 0
    for individual in population:
      if (individual['evaluation'] != 0) : continue # already available flow, tree and evaluation values (elements form elitism)
      helpers.generate_tree_flow(individual, DATA['source'])
      individual['evaluation'] = evaluation.evaluate(individual, DATA)
      sum_evalutation += individual['evaluation']
    
    # SELECTION
    sorted_population = sorted(population, key=itemgetter('evaluation'))
    best_solutions.append(sorted_population[0])
    probabilities = selection.get_probability_list(sum_evalutation, sorted_population)

    from_individual = math.floor(proposed_config['elitism'] * population_size / 100)
    new_population = sorted_population[:from_individual]
    total_done += from_individual
    
    # CROSSOVER
    total = math.floor(population_size * (proposed_config['crossover'])/ 100)
    rand_single_limit = total / 2
    crossover_index = 0
    while (crossover_index < total) :
      index_parent_1 = selection.select_roulette(population_size, probabilities, 0, probabilities[0])
      index_parent_2 = selection.select_roulette(population_size, probabilities, 0, probabilities[0])
      if (crossover_index < rand_single_limit) :
        children = crossover.crossover(first_CO, sorted_population[index_parent_1]['prufer'], sorted_population[index_parent_2]['prufer'], DATA['number_of_nodes'] - 2)
      else :
        children = crossover.crossover(second_CO, sorted_population[index_parent_1]['prufer'], sorted_population[index_parent_2]['prufer'], DATA['number_of_nodes'] - 2)
      new_individual_1 = helpers.create_new_individual()
      new_individual_2 = helpers.create_new_individual()
      new_individual_1['prufer'] = children[0]
      new_individual_2['prufer'] = children[1]
      new_population.append(new_individual_1)
      new_population.append(new_individual_2)
      crossover_index += 2
      total_done += 2
    
    # MUTATION
    from_individual += math.floor(population_size * (proposed_config['crossover'])/ 100)
    total = math.floor(population_size * (proposed_config['mutation'])/ 100)
    invasive_mutation_limit = total / 2
    mutation_index = 0
    while mutation_index < total :
      new_individual = helpers.create_new_individual()
      index_chromosome = selection.select_roulette(population_size, probabilities, 0, probabilities[0])
      if (mutation_index < invasive_mutation_limit) :
        new_individual['prufer'] = mutation.mutation(first_M, sorted_population[index_chromosome]['prufer'], DATA['number_of_nodes'] - 2)
      else :
        new_individual['prufer'] = mutation.mutation(second_M, sorted_population[index_chromosome]['prufer'], DATA['number_of_nodes'] - 2)
      new_population.append(new_individual)
      mutation_index += 1
      total_done += 1

    # HYBRID 2-opt
    if (not hybrid_outside) :
      from_individual += math.floor(population_size * (proposed_config['mutation'])/ 100)
      total = math.floor(population_size * (proposed_config['hybrid'])/ 100)
      hybrid_index = 0
      while hybrid_index < total : 
        index_chromosome = selection.select_roulette(population_size, probabilities, 0, probabilities[0])
        session_best_individual = sorted_population[index_chromosome].copy()
        session_best_individual = hybrid.opt_2(DATA, session_best_individual)
        new_population.append(session_best_individual)
        hybrid_index += 1
        total_done += 1

    # NEXT GENERATION
    population = new_population[:]

    # TERMINATION CRITERIA
    best_len = len(best_solutions)
    improvement_percentage = abs(best_solutions[best_len - 2]['evaluation'] - best_solutions[best_len - 1]['evaluation']) / best_solutions[best_len - 1]['evaluation']
    if (improvement_percentage < MINIMUM_IMPROVEMENT_TOLERANCE) :
      best_solutions_opt_counter += 1
    else :
      best_solutions_opt_counter = 0
    
    if best_solutions_opt_counter == MAX_STATIC_IMPROVEMENT : break # equal results in several iterations

  # last evaluation
  sum_evalutation = 0
  for individual in population:
    if (individual['evaluation'] != 0) : continue # already available flow, tree and evaluation values (elements form elitism)
    helpers.generate_tree_flow(individual, DATA['source'])
    individual['evaluation'] = evaluation.evaluate(individual, DATA)
    sum_evalutation += individual['evaluation']

  sorted_population = sorted(population, key=itemgetter('evaluation'))
  best_solutions.append(sorted_population[0])
  
  if (hybrid_outside) :
    probabilities = selection.get_probability_list(sum_evalutation, sorted_population)
    total = math.floor(population_size * (hybrid_outside)/ 100)
    hybrid_index = 0
    while hybrid_index < total : 
      index_chromosome = selection.select_roulette(len(sorted_population), probabilities, 0, probabilities[0])
      session_best_individual = sorted_population[index_chromosome]
      hybrid.opt_2(DATA, session_best_individual)
      hybrid_index += 1
    sorted_population = sorted(population, key=itemgetter('evaluation'))
    best_solutions.append(sorted_population[0])

  end = time.time()

  return { 'best': best_solutions, 'duration': end - start }
  

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