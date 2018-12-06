
def evaluate(population, DATA):
  for individual in population:
    heat_generation_cost = get_tree_heat_generation_cost(DATA['Betta'], DATA['T_flh'], DATA['c_heat'], DATA['source'], DATA['number_of_nodes'], individual['tree'])
    variable_investment_cost = get_tree_variable_investment_cost(DATA['c_var'], DATA['distance'], DATA['Alpha'], individual['tree'])
    revenue = calculate_revenue(DATA['c_rev'], DATA['edges_annual_demand'], DATA['Lamda'], individual['tree'])
  
  print(revenue)

def get_tree_heat_generation_cost(Betta, T_flh, c_heat, source, number_of_nodes, tree):
  heat_generation_cost = 0
  for node in range(number_of_nodes): heat_generation_cost += get_heat_generation_cost_of_node(Betta, T_flh, c_heat, source)
  return heat_generation_cost

def get_heat_generation_cost_of_node(Betta, T_flh, c_heat, source):
  val = (1 / Betta) * T_flh * c_heat[source][0] # * PI_in
  return val

def get_tree_variable_investment_cost(c_var, distance, alpha, tree):
  variable_investment_cost = 0
  for edge in tree: variable_investment_cost += get_variable_investment_cost_in_edge(c_var, distance, alpha, edge[0], edge[1])
  return variable_investment_cost

def get_variable_investment_cost_in_edge(c_var, distance, alpha, from_vertex, to_vertex):
  return alpha * distance[from_vertex][to_vertex] * c_var[from_vertex][to_vertex] #* P_in

#calculate revenue
def calculate_revenue(c_rev, annual_demand, lamda, prufer_to_tree):
  total_revenue = 0
  for item in prufer_to_tree: 
    edge_c_rev = c_rev[item[0]][item[1]]
    edge_annual_demand = annual_demand[item[0]][item[1]]
    total_revenue += edge_c_rev * edge_annual_demand 
 
  scaled_total_revenue = lamda * total_revenue
  return  scaled_total_revenue

#calculate unmet demand penalty
def calculate_unmet_demand_penalty(factor, c_umd, annual_demand, tree):
  total_umt_dem_pen = 0
  for edge in tree:
    edge_peak_dem  = edges_peak_demand[edge[0]][edge[1]]
    edge_len = edge_length[edge[0]][edge[1]]
    mytl_fix  = tl_fix[edge[0]][edge[1]]
    mytl_var  = tl_var[edge[0]][edge[1]]
    total_umt_dem_pen += edge_peak_dem - ((mytl_fix + mytl_var) * edge_len)

  return total_umt_dem_pen


