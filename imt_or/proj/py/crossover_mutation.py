import math
import random

def single_point_CO(parent_1, parent_2, length, middle):
  child_1 = parent_1[:middle] + parent_2[middle:]
  child_2 = parent_2[:middle] + parent_1[middle:]
  return child_1, child_2

def second_point_CO(parent_1, parent_2, length):
  len_point = math.floor(length / 3)
  plus_one = 0 if (length%2 == 0) else 1
  child_1 = parent_1[:len_point] + parent_2[len_point:(2 * len_point + plus_one)] + parent_1[(2 * len_point + plus_one):]
  child_2 = parent_2[:len_point] + parent_1[len_point:(2 * len_point + plus_one)] + parent_2[(2 * len_point + plus_one):]
  return child_1, child_2

def allele_flip_M(chromosome, length):
  rand = random.randint(0, length - 1)
  chromosome[rand] = random.randint(0, length - 1)

def insertion_M(chromosome, length):
  rand_from = random.randint(0, length - 1)
  rand_to = random.randint(0, length - 1)
  print(rand_from)
  print(rand_to)
  chromosome.insert(rand_to, chromosome[rand_from]) 
  index_add = 1 if (rand_to < rand_from) else 0
  chromosome.pop(rand_from + index_add)


#def k_point_CO(parent_1, parent_2, length, k):
#  len_point = math.floor(length / k)
#  if (len_point == 0) : return parent_1, parent_2
 