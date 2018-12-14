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
def get_tree_based_population(N, number_nodes):
  population_arr = []
  for n in range(N): 
    individual = {'prufer': [], 'tree': [], 'flow': {}, 'evaluation': 0}
    individual['prufer'] = create_prufer_sequence(number_nodes)
    population_arr.append(individual)
  return population_arr

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

  #calculate revenue
def calculate_revenue(c_rev,dist,lamda,prufer_to_tree):
  total_revenue = 0
  for item in prufer_to_tree: 
    my_crev = c_rev[item[0]][item[1]]
    mydist  = dist[item[0]][item[1]]
    #print(my_crev)
    total_revenue += my_crev * mydist 
 
  #print(total_revenue)
  scaled_total_revenue = lamda * total_revenue
  return  scaled_total_revenue
#calculate unmet demand penalty
def calculate_unmet_demand_penalty(edges_peak_demand,cumd,prufer_to_tree):
  total_umt_dem_pen = 0
  for item in prufer_to_tree:
    edge_peak_dem  = edges_peak_demand[item[0]][item[1]]
    mycumd  = cumd[item[0]][item[1]]
    #edge_len = edge_length[item[0]][item[1]]
    #ytl_var  = tl_var[item[0]][item[1]]
    total_umt_dem_pen += 0.5 * mycumd * edge_peak_dem 

  return total_umt_dem_pen

#fixed investment cost
def calculate_fixed_investment_cost(alpha,c_fix,edge_length,prufer_to_tree):
  total_fixed_investment_cost = 0
  for item in prufer_to_tree:
    c_fixed  = c_fix[item[0]][item[1]]
    edge_len = edge_length[item[0]][item[1]]
    total_fixed_investment_cost += c_fixed * edge_len

  return total_fixed_investment_cost * alpha

#fixed investment cost
def calculate_maitenance_cost(c_om,edge_length,prufer_to_tree):
  total_maitenance_cost = 0
  for item in prufer_to_tree:
    c_omm  = c_om[item[0]][item[1]]
    edge_len = edge_length[item[0]][item[1]]
    total_maitenance_cost +=  c_omm * edge_len
  return total_maitenance_cost