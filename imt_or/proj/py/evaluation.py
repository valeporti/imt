import helpers
import pprint as pp
import numpy as np

def evaluate(individual, DATA):
  Total_P_in = calculate_power_flow(individual['flow'], individual['tree'], DATA)
  heat_generation_cost = get_tree_heat_generation_cost(DATA['Betta'], DATA['T_flh'], DATA['c_heat'], DATA['P_in'], DATA['source'], individual['flow'])
  revenue = calculate_revenue(DATA['c_rev'], DATA['edges_annual_demand'], DATA['Lamda'], individual['tree'])
  maintenance_cost = get_tree_maintenance_cost(DATA['c_om'], DATA['distance'], individual['tree'])
  fixed_investment_cost = get_fixed_investment_cost(DATA['c_fix'], DATA['distance'], DATA['Alpha'], individual['tree'])
  variable_investment_cost = get_tree_variable_investment_cost(DATA['c_var'], DATA['distance'], DATA['Alpha'], DATA['P_in'], individual['tree'])
  unmet_demand_penalty = get_tree_unmet_demand_penalty(DATA['p_umd'], DATA['edges_annual_demand'], individual['tree'], DATA['number_of_nodes'])
  """ print(revenue)
  print(heat_generation_cost)
  print(maintenance_cost)
  print(fixed_investment_cost)
  print(variable_investment_cost)
  print(unmet_demand_penalty) """
  total_expenses = (heat_generation_cost + maintenance_cost + fixed_investment_cost + variable_investment_cost + unmet_demand_penalty) - revenue
  DATA['P_in'] = []
  return total_expenses

def get_tree_unmet_demand_penalty(p_umd, edges_annual_demand, tree, number_of_nodes) :
  unmet_demand_penalty = 0
  for i in range(number_of_nodes) :
    for j in range(number_of_nodes) :
      if ((i,j) not in tree and (j, i) not in tree): unmet_demand_penalty += p_umd[i][j] * edges_annual_demand[i][j]
  return unmet_demand_penalty * 0.5
  

def get_tree_variable_investment_cost(c_var, distance, Alpha, P_in, tree) :
  variable_investment_cost = 0
  for edge in tree : variable_investment_cost += c_var[edge[0]][edge[1]] * distance[edge[0]][edge[1]] * P_in[edge[0]][edge[1]]
  return variable_investment_cost * Alpha 

def get_fixed_investment_cost(c_fix, distance, Alpha, tree) :
  investment_cost = 0
  for edge in tree : investment_cost += c_fix[edge[1]][edge[0]] * distance[edge[1]][edge[0]]
  return investment_cost * Alpha

def get_tree_maintenance_cost(c_om, distance, tree) :
  maintenance_cost = 0
  for edge in tree : maintenance_cost += c_om[edge[0]][edge[1]] * distance[edge[0]][edge[1]]
  return maintenance_cost

def get_tree_heat_generation_cost(Betta, T_flh, c_heat, P_in, source, flow):
  heat_generation_cost = 0
  flow_tree_source = flow['flow_tree'][source]
  for to_vertex in flow_tree_source['child'] : heat_generation_cost += (1 / Betta) * T_flh * c_heat[source][0] * P_in[source][to_vertex]
  return heat_generation_cost

def calculate_power_flow(flow, tree, DATA):
  remaining_tree = tree[:] 
  P_in_arr = np.zeros((DATA['number_of_nodes'],DATA['number_of_nodes']))
  P_in = find_edge_power_flow([DATA['source']], remaining_tree, -1, DATA, P_in_arr)
  DATA['P_in'] = P_in_arr
  return P_in

def find_edge_power_flow(nodes, remaining_tree, parent, DATA, P_in_arr):

  if len(nodes) == 0 : return 0 # P_out  = 0 in leaf
  
  P_in = 0
  children = []
  for node in nodes :
    children = helpers.search_node_children(remaining_tree, node) # get children of node, remove
    for child in children :
      P_out = find_edge_power_flow([child], remaining_tree, node, DATA, P_in_arr)
      #print('[' + str(node) + ', ' + str(child) + ']')
      Etta = 1 - DATA['distance'][node][child] * DATA['v_var'][node][child]
      Delta = DATA['Betta'] * DATA['Lamda'] * DATA['edges_peak_demand'][node][child] + DATA['distance'][node][child] * DATA['v_fix'][node][child]  
      value = (Delta + P_out) / Etta
      P_in += value
      P_in_arr[node][child] = value
      P_in_arr[child][node] = value
    
  return P_in

def calculate_revenue(c_rev, annual_demand, lamda, prufer_to_tree):
  total_revenue = 0
  for item in prufer_to_tree: 
    edge_c_rev = c_rev[item[0]][item[1]]
    edge_annual_demand = annual_demand[item[0]][item[1]]
    total_revenue += edge_c_rev * edge_annual_demand 
 
  scaled_total_revenue = lamda * total_revenue
  return  scaled_total_revenue

def calculate_unmet_demand_penalty(factor, c_umd, annual_demand, tree):
  total_umt_dem_pen = 0
  for edge in tree:
    edge_peak_dem  = edges_peak_demand[edge[0]][edge[1]]
    edge_len = edge_length[edge[0]][edge[1]]
    mytl_fix  = tl_fix[edge[0]][edge[1]]
    mytl_var  = tl_var[edge[0]][edge[1]]
    total_umt_dem_pen += edge_peak_dem - ((mytl_fix + mytl_var) * edge_len)

  return total_umt_dem_pen


