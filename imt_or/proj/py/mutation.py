import math
import random

def mutation(option, chromosome, length) :
  chromosome = chromosome[:]
  if (option == 0) :
    choice = random.randint(0, 1)
    if (choice == 0) :
      allele_flip_M(chromosome, length)
    elif (choice == 1) :
      insertion_M(chromosome, length)
  elif (option == 1) :
    allele_flip_M(chromosome, length)
  elif (option == 2) :
    insertion_M(chromosome, length)
  return chromosome

def allele_flip_M(chromosome, length):
  rand = random.randint(0, length - 1)
  chromosome[rand] = random.randint(0, length - 1)

def insertion_M(chromosome, length):
  rand_from = random.randint(0, length - 1)
  rand_to = random.randint(0, length - 2)
  temp = chromosome[rand_from]
  chromosome.pop(rand_from)
  chromosome.insert(rand_to, temp) 
  
