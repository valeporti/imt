import math
import random

def crossover(option, parent_1, parent_2, length) :
  children = []
  if (option == 0) :
    choice = random.randint(0, 2)
    if (choice == 0) :
      children = single_point_CO(parent_1, parent_2, length)
    elif (choice == 1) :
      children = second_point_CO(parent_1, parent_2, length)
    elif (choice == 2) :
      children = rand_single_CO(parent_1, parent_2, length)
    elif (choice == 3) :
      children = min_max_rand_CO(parent_1, parent_2, length)
  elif (option == 1) :
    children = single_point_CO(parent_1, parent_2, length)
  elif (option == 2) :
    children = second_point_CO(parent_1, parent_2, length)
  elif (option == 3) :
    children = rand_single_CO(parent_1, parent_2, length)
  elif (option == 4) :
    children = min_max_rand_CO(parent_1, parent_2, length)
  else :
    print('else')

  return children
    

def single_point_CO(parent_1, parent_2, length):
  middle = math.floor(length / 2)
  child_1 = parent_1[:middle] + parent_2[middle:]
  child_2 = parent_2[:middle] + parent_1[middle:]
  return child_1, child_2

def second_point_CO(parent_1, parent_2, length):
  len_point = math.floor(length / 3)
  plus_one = 0 if (length%2 == 0) else 1
  child_1 = parent_1[:len_point] + parent_2[len_point:(2 * len_point + plus_one)] + parent_1[(2 * len_point + plus_one):]
  child_2 = parent_2[:len_point] + parent_1[len_point:(2 * len_point + plus_one)] + parent_2[(2 * len_point + plus_one):]
  return child_1, child_2

def rand_single_CO(parent_1, parent_2, length):
  pos = random.randint(0, length)
  return parent_1[:pos] + parent_2[pos:], parent_2[:pos] + parent_1[pos:]

def min_max_rand_CO(parent_1, parent_2, length):
  pos_a = random.randint(0, length)
  pos_b = random.randint(0, length)
  child1 = []
  child2 = []
  start_pos = min(pos_a, pos_b)
  end_pos = max(pos_a, pos_b)
  for i in range(start_pos, end_pos):
    child1.append(parent_1[i])
  child2 = [item for item in parent_2 if item not in child1]
  return parent_2[:start_pos] + child1, child2



#def k_point_CO(parent_1, parent_2, length, k):
#  len_point = math.floor(length / k)
#  if (len_point == 0) : return parent_1, parent_2
 