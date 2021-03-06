import helpers
import random
import evaluation
import helpers
import pprint as pp

def opt_2(DATA, session_best_individual) :

  for j in range(DATA['number_of_nodes'] - 2) :
    index = 0
    index_plus_one = 0
    while (index < DATA['number_of_nodes'] - 2) : 
      new_individual = helpers.create_new_individual()
      new_individual['prufer'] = session_best_individual['prufer'][:]

      index_rand = random.randint(0, DATA['number_of_nodes'] - 2 - 1)
      switch(new_individual['prufer'], j, index_rand)

      helpers.generate_tree_flow(new_individual, DATA['source'])
      new_individual['evaluation'] = evaluation.evaluate(new_individual, DATA)

      if (new_individual['evaluation'] < session_best_individual['evaluation']) :
        session_best_individual = new_individual.copy()

      index_plus_one += 1
      index += index_plus_one
  return session_best_individual


def switch(chromosome, from_index, to_index) :
  tmp = chromosome[from_index]
  chromosome[from_index] = chromosome[to_index]
  chromosome[to_index] = tmp

