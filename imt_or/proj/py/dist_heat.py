import helpers


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
number_of_nodes = 8

## GA Algorithm Implementation
population_size = 3

# POPULATION
population = helpers.get_tree_based_population(population_size, number_of_nodes)
print(population)

# EVALUATION OF INDIVUDUALS IN POPULATION

# SELECTION

# CROSSOVER AND MUTATION

# NEXT GENERATION

# TERMINATION CRITERIA
