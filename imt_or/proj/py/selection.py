import random

def select_roulette(size, probabilities):
  rand = random.uniform(0,probabilities[0])
  for j in range (size) :
    if (j + 1 < size and rand > probabilities[j + 1]) :
      return j
    if (j + 1 == size):
      return j

def get_probability_list(total_fit, population):
  relative_fitness = [individual['evaluation']/total_fit for individual in population]
  probabilities = [sum(relative_fitness[i:]) for i in range(len(relative_fitness))]
  return probabilities
