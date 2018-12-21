import dist_heat
import helpers
import pprint as pp
import pandas 
from operator import itemgetter, attrgetter
import os

# try with percentages of elite, crossover, mutatuon, elitism
# try with different combinations of algorithms for mutation and crossover

def run_GA(tries, DATA, C_1, C_2, M_1, M_2, itera, pop_size, hy_out, conf, dir, file) :
  
  if not os.path.exists(dir + '/'):
    os.makedirs(dir + '/')
  
  all_iterations = []

  for i in range(tries) :
    # Defined configuration, several tries
    results = dist_heat.genetic_algorithm_district_heating(DATA, itera, pop_size, hy_out, conf, C_1, C_2, M_1, M_2)
    best_solutions = results['best']
    best_solutions = sorted(best_solutions, key=itemgetter('evaluation'))
    all_iterations.append({'crossover': conf['crossover'], 'mutation': conf['mutation'],'crossover_1': C_1,'crossover_2': C_2,'mutation_1': M_1, 'mutation_2': M_2,'elitism': conf['elitism'],'hybrid': conf['hybrid'],'hybrid_outside' : hy_out, 'best': best_solutions[0], 'duration': results['duration'], 'evaluation': best_solutions[0]['evaluation'],'population': pop_size,'iterations': itera,})
    print('eval best solution: ' + str(best_solutions[0]['evaluation']))
    print('duration: ' + str(results['duration']))
    print('try #' + str(i))
  
  all_iterations = sorted(all_iterations, key=itemgetter('evaluation'))
  series_big_data = pandas.Series(all_iterations)
  data_frame_big_data = pandas.DataFrame(all_iterations, index=series_big_data.index, columns=['evaluation', 'best', 'population', 'iterations', 'duration', 'hybrid', 'hybrid_outside', 'mutation', 'elitism', 'crossover', 'crossover_1', 'crossover_2', 'mutation_1', 'mutation_2'])
  data_frame_big_data.to_pickle(dir + '/' + file + '.pkl')
