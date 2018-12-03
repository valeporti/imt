import helpers
import evaluation
import crossover_mutation as cm
import math
import pprint as pp


# DATA
excel_file = 'smalldata.xlsx'

nodes_coord = helpers.read_excel_data(excel_file, 'NodesCord')
#FixedUnitCost = helpers.read_excel_data(excel_file, 'FixedUnitCost')[0][0]
c_rev = helpers.read_excel_data(excel_file, 'crev')
c_om = helpers.read_excel_data(excel_file, 'com')
c_heat = helpers.read_excel_data(excel_file, 'cheat')
c_var = helpers.read_excel_data(excel_file, 'cvar')
p_umd = helpers.read_excel_data(excel_file, 'pumd')
v_var = helpers.read_excel_data(excel_file, 'vvar')
v_fix = helpers.read_excel_data(excel_file, 'vfix')
T_flh = helpers.read_excel_data(excel_file, 'Tflh')
Betta = helpers.read_excel_data(excel_file, 'Betta')[0][0]
Gamma = helpers.read_excel_data(excel_file, 'Gamma')[0][0]
Alpha = helpers.read_excel_data(excel_file, 'Alpha')[0][0]
edges_peak_demand = helpers.read_excel_data(excel_file, 'EdgesDemandPeak')
edges_annual_demand = helpers.read_excel_data(excel_file, 'EdgesDemandAnnual')
C_max = helpers.read_excel_data(excel_file, 'Cmax')
Q_max = helpers.read_excel_data(excel_file, 'SourceMaxCap')[0][0]

source_num = helpers.read_excel_data(excel_file, 'SourceNum')[0][0]
number_of_nodes = len(nodes_coord)

distance_matrix = helpers.distance_between_edges_matrix(nodes_coord, number_of_nodes)

#DATA = {'a': c_om,'b': c_rev} 
#print(DATA)

## GA Algorithm Implementation
population_size = 3

# POPULATION INITIALIZATION
population = helpers.get_tree_based_population(population_size, number_of_nodes)
print(population[0])
print(population)
population[0]['tree'] = helpers.prufer_to_tree(population[0]['prufer'])
print(population[0]['tree'])
arr1 = [1, 2, 3, 4, 5, 6]
arr2 = [8, 9, 10, 11, 12, 13]

let = cm.single_point_CO(arr1, arr2, len(arr1), math.floor((7)/2) )
print(let)
let2 = cm.second_point_CO(arr1, arr2, len(arr1))
print(let2)
let3 = cm.allele_flip_M(let2[0], len(arr1))
print(let2[0])

arr3 = [1, 2,3, 4, 5]
cm.insertion_M(arr3, len(arr3))
print(arr3)

#prufer_Of_individual = helpers.prufer_to_tree(population[0]['prufer']
#population[0]['tree'] = helpers.prufer_to_tree(population[0]['prufer'])
#print(population[0])
#for n in helpers.prufer_to_tree(population[0]['tree']:


# EVALUATION OF INDIVUDUALS IN POPULATION

# SELECTION

# CROSSOVER AND MUTATION

# NEXT GENERATION

# TERMINATION CRITERIA
