import pandas as pd
import random
import math

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
    individual = {'prufer': [], 'tree': [], 'flow': {}, 'evaluation': 0}
    individual['prufer'] = create_prufer_sequence(number_nodes)
    individual['tree'] = prufer_to_tree(individual['prufer'])
    #individual['tree'] = [(0,3), (1,0), (2,1), (3,7), (4,2), (4,5), (5,6)]
    individual['flow'] = get_flow_from_tree(source, individual['tree'])
    population_arr.append(individual)
  return population_arr

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