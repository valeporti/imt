
def heat_generation_cost_of_node(beta, T_flh, c_heat, source):
  return (1 / beta) * T_flh * c_heat[source]

def variable_investment_cost(c_var, distance, alpha, from_vertex, to_vertex):
  return alpha * distance[from_vertex][to_vertex] * c_var[from_vertex][to_vertex]

#calculate revenue
def calculate_revenue(c_rev, dist, lamda, prufer_to_tree):
  total_revenue = 0
  for item in prufer_to_tree: 
    my_crev = c_rev[item[0]][item[1]]
    mydist  = dist[item[0]][item[1]]
    #print(my_crev)
    total_revenue += my_crev + mydist 
 
  #print(total_revenue)
  scaled_total_revenue = lamda * total_revenue
  return  scaled_total_revenue

#calculate unmet demand penalty
def calculate_unmet_demand_penalty(edges_peak_demand, edge_length, tl_fix, tl_var, prufer_to_tree):
  total_umt_dem_pen = 0
  for item in prufer_to_tree:
    edge_peak_dem  = edges_peak_demand[item[0]][item[1]]
    edge_len = edge_length[item[0]][item[1]]
    mytl_fix  = tl_fix[item[0]][item[1]]
    mytl_var  = tl_var[item[0]][item[1]]
    total_umt_dem_pen += edge_peak_dem - ((mytl_fix + mytl_var) * edge_len)

  return total_umt_dem_pen


