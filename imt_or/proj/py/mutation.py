import math
import random

DISPLACEMENT_OPTION = 0
INVERSMENT_OPTION = 1
DISPLACED_INVERSION_OPTION = 2

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
  elif (option == 3) :
    inv_and_or_disp_M(DISPLACEMENT_OPTION, chromosome, length)
  elif (option == 4) :
    inv_and_or_disp_M(INVERSMENT_OPTION, chromosome, length)
  elif (option == 5) :
    inv_and_or_disp_M(DISPLACED_INVERSION_OPTION, chromosome, length)
  elif (option == 6) :
    invasive_allele_flip_M(chromosome, length)
  elif (option == 7) :
    chromosome = rand_displacement_M(chromosome)
  elif (option == 8) :
    chromosome = rand_displaced_inversion_M(chromosome)
  return chromosome

def allele_flip_M(chromosome, length):
  rand = random.randint(0, length - 1)
  chromosome[rand] = random.randint(0, length - 1)

def invasive_allele_flip_M(chromosome, length) :
  index = 0
  index_plus_one = 0
  while (index < length) :
    index_rand = random.randint(0, length - 1)
    chromosome[index_rand] = random.randint(0, length - 1)
    index_plus_one += 1
    index += index_plus_one
    

def insertion_M(chromosome, length):
  rand_from = random.randint(0, length - 1)
  temp = chromosome[rand_from]
  chromosome.pop(rand_from)
  rand_to = random.randint(0, length - 2) # already poped out one element 
  chromosome.insert(rand_to, temp) 

def inv_and_or_disp_M(option, chromosome, length) :
  rand_1 = random.randint(0, length - 1)
  rand_2 = random.randint(0, length - 1)
  rand_start = min(rand_1, rand_2)
  rand_end = max(rand_1, rand_2)
  length_change = rand_end - rand_start + 1
  rand_to = random.randint(0, length - length_change)
  #print(rand_start)
  #print(rand_end)
  #print(rand_to)
  if (option == DISPLACEMENT_OPTION) :
    displacement_M(chromosome, length_change, rand_start, rand_to)
  elif (option == INVERSMENT_OPTION) :
    inversion_M(chromosome, length_change, rand_start, rand_end) 
  elif (option == DISPLACED_INVERSION_OPTION) : 
    inversion_M(chromosome, length_change, rand_start, rand_end) 
    displacement_M(chromosome, length_change, rand_start, rand_to)

def inversion_M(chromosome, length_change, rand_start, rand_end):
  for i in range(math.floor(length_change/2)) :
    tmp = chromosome[rand_end - i]
    chromosome[rand_end - i] = chromosome[rand_start + i]
    chromosome[rand_start + i] = tmp

def displacement_M(chromosome, length_change, rand_start, rand_to) :
  temp_list = chromosome[rand_start:rand_start + length_change]
  del chromosome[rand_start:rand_start + length_change]
  for i in range(length_change) :
    chromosome.insert(rand_to + i, temp_list[i])

def rand_displacement_M(individual):
	
	my_individual = individual
	first_rnd = random.randint(0,len(my_individual )-1)
	sec_rnd = random.randint(0,len(my_individual )-1)
	t_rnd = random.randint(0,len(my_individual )-1)
	""" print ('R1 : ' + str(first_rnd))
	print ('R2 : ' + str(sec_rnd))
	print ('R3 : ' + str(t_rnd))
	print ('Array Length : ' + str(len(my_individual ))) """
	if sec_rnd != first_rnd:
		if  sec_rnd > first_rnd:
			#print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
			#print('R2 > R1')
			return shift(my_individual,first_rnd,sec_rnd, t_rnd)
		else:
			#print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
			
			#print('R1 > R2')
			return shift(my_individual,sec_rnd,first_rnd, t_rnd)
	return my_individual

def rand_displaced_inversion_M(individual):

	my_individual = individual
	first_rnd = random.randint(0,len(my_individual )-1)
	sec_rnd = random.randint(0,len(my_individual )-1)
	t_rnd = random.randint(0,len(my_individual )-1)
	""" print ('R1 : ' + str(first_rnd))
	print ('R2 : ' + str(sec_rnd))
	print ('R3 : ' + str(t_rnd))
	print ('Array Length : ' + str(len(my_individual ))) """
	if sec_rnd != first_rnd:
		if  sec_rnd > first_rnd:
			#print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
			#print('R2 > R1')
			return shift_dis_inversion(my_individual,first_rnd,sec_rnd, t_rnd)
		else:
			#print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
			#print('R1 > R2')
			return shift_dis_inversion(my_individual,sec_rnd,first_rnd, t_rnd)
	return my_individual

def shift(L, start, end, insert_at):
	#transindividual = []
	cutrray = []
	rem_array =[]
	#print('Genes of Individual')
	#for i in range(len(L)):
		#print(L[i])
	for i in range(start, end + 1 ,1):
		cutrray.append(L[i])
	for i in range(start-1,-1,-1):
		rem_array.append(L[i])
	if start != len(L) - 1:
		for i in range(len(L) - 1,end,-1):
			rem_array.append(L[i])
	else:
		for i in range(end,len(L) - 1,1):
			rem_array.append(L[i])
	#print('Cut array'+ str(cutrray))
	#print('Rem array'+ str(rem_array))
	pos = insert_at
	for i in range(len(cutrray)):
		rem_array.insert(pos, cutrray[i])
		pos = pos + 1
	#print('Trans array'+ str(rem_array))
	return rem_array

def shift_dis_inversion(L, start, end, insert_at):
	#transindividual = []
	cutrray = []
	rem_array =[]
	#print('Genes of Individual')
	#for i in range(len(L)):
		#print(L[i])
	for i in range(start, end + 1 ,1):
		cutrray.append(L[i])
	for i in range(start-1,-1,-1):
		rem_array.append(L[i])
	if start != len(L) - 1:
		for i in range(len(L) - 1,end,-1):
			rem_array.append(L[i])
	else:
		for i in range(end,len(L) - 1,1):
			rem_array.append(L[i])
	#print('Cut array'+ str(cutrray))
	#print('Rem array'+ str(rem_array))
	pos = insert_at
	for i in range(len(cutrray)):
		cutrray.reverse()
		rem_array.insert(pos, cutrray[i])
		pos = pos + 1
	#print('Trans array'+ str(rem_array))
	return rem_array
