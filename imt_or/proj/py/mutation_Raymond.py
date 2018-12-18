import random


def inversion_mutation(individual):
	my_individual = individual
	first_rnd = random.randint(0,len(my_individual )-1)
	sec_rnd = random.randint(0,len(my_individual )-1)
	t_rnd = random.randint(0,len(my_individual )-1)
	print ('R1 : ' + str(first_rnd))
	#print ('R : ' + str(sec_rnd))
	print ('R2 : ' + str(t_rnd))
	print ('Array Length : ' + str(len(my_individual )))

	#for i in range(len(my_individual )):
		#print(my_individual[i])

	print(shift(my_individual,first_rnd,first_rnd, t_rnd))
	return

def displacement_mutation(individual):
	
	my_individual = individual
	first_rnd = random.randint(0,len(my_individual )-1)
	sec_rnd = random.randint(0,len(my_individual )-1)
	t_rnd = random.randint(0,len(my_individual )-1)
	print ('R1 : ' + str(first_rnd))
	print ('R2 : ' + str(sec_rnd))
	print ('R3 : ' + str(t_rnd))
	print ('Array Length : ' + str(len(my_individual )))
	if sec_rnd != first_rnd:
		if  sec_rnd > first_rnd:
			#print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
			print('R2 > R1')
			print(shift(my_individual,first_rnd,sec_rnd, t_rnd))
		else:
			#print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
			
			print('R1 > R2')
			print(shift(my_individual,sec_rnd,first_rnd, t_rnd))
			#print(transindividual)
	return

def displaced_inversion_mutation(individual):

	my_individual = individual
	first_rnd = random.randint(0,len(my_individual )-1)
	sec_rnd = random.randint(0,len(my_individual )-1)
	t_rnd = random.randint(0,len(my_individual )-1)
	print ('R1 : ' + str(first_rnd))
	print ('R2 : ' + str(sec_rnd))
	print ('R3 : ' + str(t_rnd))
	print ('Array Length : ' + str(len(my_individual )))
	if sec_rnd != first_rnd:
		if  sec_rnd > first_rnd:
			#print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
			print('R2 > R1')
			print(shift_dis_inversion(my_individual,first_rnd,sec_rnd, t_rnd))
		else:
			#print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
			
			print('R1 > R2')
			print(shift_dis_inversion(my_individual,sec_rnd,first_rnd, t_rnd))
			#print(transindividual)
	return

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
	if start != len(L):
		print('say what')
		for i in range(len(L),end,-1):
			rem_array.append(L[i])
	else:
		for i in range(end,len(L),1):
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
	if start != len(L):
		for i in range(len(L),end,-1):
			rem_array.append(L[i])
	else:
		for i in range(end,len(L),1):
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


