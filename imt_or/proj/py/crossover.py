import math
import random

def crossover(option, parent_1, parent_2, length) :
  children = []
  if (option == 0) :
    choice = random.randint(0, 3)
    if (choice == 0) :
      children = single_point_CO(parent_1, parent_2, length)
    elif (choice == 1) :
      children = second_point_CO(parent_1, parent_2, length)
    elif (choice == 2) :
      children = rand_single_CO(parent_1, parent_2, length)
    elif (choice == 3) :
      children = rand_two_CO(parent_1, parent_2, length)
    elif (choice == 4) :
      children = uniform_CO(parent_1, parent_2, length)
  elif (option == 1) :
    children = rand_single_CO(parent_1, parent_2, length)
  elif (option == 2) :
    children = rand_two_CO(parent_1, parent_2, length)
  elif (option == 3) :
    children = uniform_CO(parent_1, parent_2, length)
  elif (option == 4) :
    children = single_point_CO(parent_1, parent_2, length)
  elif (option == 5) :
    children = second_point_CO(parent_1, parent_2, length)
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

def rand_two_CO(parent_1, parent_2, length):
  pos_a = random.randint(0, length)
  pos_b = random.randint(0, length)
  start_pos = min(pos_a, pos_b)
  end_pos = max(pos_a, pos_b)
  child_1 = parent_1[:start_pos] + parent_2[start_pos:end_pos] + parent_1[end_pos:]
  child_2 = parent_2[:start_pos] + parent_1[start_pos:end_pos] + parent_2[end_pos:]
  return child_1, child_2

def uniform_CO(parent_1, parent_2, length):
  arr = [random.randint(0,1) for i in range(length)]
  child_1 = []
  child_2 = []
  for i in range(length) :
    if (arr[i] == 1) :
      child_1.append(parent_1[i])
      child_2.append(parent_2[i])
    else :
      child_1.append(parent_2[i])
      child_2.append(parent_1[i])
  return child_1, child_2

 