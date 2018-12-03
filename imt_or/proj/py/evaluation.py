
def heat_generation_cost_of_node(beta, T_flh, c_heat, source):
  return (1 / beta) * T_flh * c_heat[source]

def variable_investment_cost(c_var, distance, alpha, from_vertex, to_vertex):
  return alpha * distance[from_vertex][to_vertex] * c_var[from_vertex][to_vertex]



