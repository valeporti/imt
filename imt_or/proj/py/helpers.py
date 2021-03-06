import pandas as pd
import random
import math
#from sympy.combinatorics.prufer import Prufer

def get_data(file_name):
  excel_file = file_name
  nodes_coord = read_excel_data(excel_file, 'NodesCord')
  number_of_nodes = len(nodes_coord)
  distance_matrix = distance_between_edges_matrix(nodes_coord, number_of_nodes)
  return {
    'c_rev': read_excel_data(excel_file, 'crev'),
    'c_om': read_excel_data(excel_file, 'com'),
    'c_heat': read_excel_data(excel_file, 'cheat'),
    'c_var': read_excel_data(excel_file, 'cvar'),
    'c_fix': read_excel_data(excel_file, 'cfix'),
    'p_umd': read_excel_data(excel_file, 'pumd'),
    'v_var': read_excel_data(excel_file, 'vvar'),
    'v_fix': read_excel_data(excel_file, 'vfix'),
    'T_flh': read_excel_data(excel_file, 'Tflh')[0][0],
    'Betta': read_excel_data(excel_file, 'Betta')[0][0],
    'Lamda': read_excel_data(excel_file, 'Gamma')[0][0],
    'Alpha': read_excel_data(excel_file, 'Alpha')[0][0],
    'edges_peak_demand': read_excel_data(excel_file, 'EdgesDemandPeak'),
    'edges_annual_demand': read_excel_data(excel_file, 'EdgesDemandAnnual'),
    'C_max': read_excel_data(excel_file, 'Cmax'),
    'Q_max': read_excel_data(excel_file, 'SourceMaxCap')[0][0],
    'source': read_excel_data(excel_file, 'SourceNum')[0][0] - 1,
    'distance': distance_matrix,
    'number_of_nodes': number_of_nodes
  }

# DATA FUNCTIONS
def read_excel_data(filename, sheet_name):
  data = pd.read_excel(filename, sheet_name=sheet_name, header=None)
  values = data.values
  return values

def distance_between_edges_matrix(coordinates, number_nodes) :
  matrix = []
  for j in range(number_nodes):
    arr = []
    for i in range(number_nodes):
      distance = distance_between_two_coordinates(coordinates[j], coordinates[i])
      arr.append(distance)

    matrix.append(arr)

  return matrix

def distance_between_two_coordinates(c1, c2) :
  distance = math.sqrt((c1[0] - c2[0]) * (c1[0] - c2[0]) + (c1[1] - c2[1]) * (c1[1] - c2[1]))
  return distance

# POPULATION FUNCTIONS
def get_tree_based_population(N, number_nodes, source):
  population_arr = []
  for n in range(N): 
    individual = create_new_individual()
    individual['prufer'] = create_prufer_sequence(number_nodes)
    population_arr.append(individual)
  return population_arr

def generate_tree_flow(individual, source) : 
  #individual['prufer'] = [5, 4, 2, 1, 0, 3]
  individual['tree'] = prufer_to_tree(individual['prufer'])
  #individual['tree'] = [(0,3), (1,0), (2,1), (3,7), (4,2), (4,5), (5,6)]
  #individual['prufer'] = Prufer(individual['tree']).prufer_repr
  individual['flow'] = get_flow_from_tree(source, individual['tree'])

def create_new_individual() :
  return {'prufer': [], 'tree': [], 'flow': {}, 'evaluation': 0}

def initialize_individual(individual) :
  individual['prufer'] = []
  individual['tree'] = []
  individual['flow'] = {}
  individual['evaluation'] = 0

def get_flow_from_tree(source, tree):

  remaining_tree = tree[:] # in order to be able to manipulate it and maintain the original one
  flow = {'root': source, 'leaves': [], 'flow_tree': {}}
  find_path_on_tree([source], remaining_tree, -1, flow)

  return flow

def find_path_on_tree(nodes, remaining_tree, parent, flow):

  if len(nodes) == 0 : # recursion end condition
    flow['leaves'].append(parent) # as is the en of recursion, means it's a leaf
    return -1

  for node in nodes:
    children = search_node_children(remaining_tree, node) # get children of node, remove
    # already information of a particular node, add it to the flow dictionary
    flow['flow_tree'][node] = {'parent': -1, 'child': []}
    flow['flow_tree'][node]['child'] = children
    flow['flow_tree'][node]['parent'] = parent
    # recursion, next node analysis (children, parent)
    find_path_on_tree(children, remaining_tree, node, flow) 


def search_node_children(remaining_tree, node) :

  children = []
  length = len(remaining_tree)
  i = 0

  while i < length:
    edge = remaining_tree[i]
    if node in edge:
      children.append(edge[0] if (edge[0] != node) else edge[1])
      remaining_tree.remove(edge)
      length -= 1 # update lenght since removed element
      i -= 1 # update index since removed element
    i += 1
  return children

def create_prufer_sequence(number_nodes):
  arr = [random.randint(0, number_nodes - 1) for i in range(number_nodes - 2)]
  return arr

def prufer_to_tree(prufer_arr): # https://hamberg.no/erlend/posts/2010-11-06-prufer-sequence-compact-tree-representation.html
  tree = []
  T = range(0, len(prufer_arr)+2)

  # the degree of each node is how many times it appears
  # in the sequence
  deg = [1]*len(T)
  for i in prufer_arr: deg[i] += 1

  # for each node label i in a, find the first node j with degree 1 and add
  # the edge (j, i) to the tree
  for i in prufer_arr:
    for j in T:
      if deg[j] == 1:
        tree.append((i,j))
        # decrement the degrees of i and j
        deg[i] -= 1
        deg[j] -= 1
        break

  last = [x for x in T if deg[x] == 1]
  tree.append((last[0],last[1]))

  return tree