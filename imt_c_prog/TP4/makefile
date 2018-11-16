makefile: 2.1.o helpers.o sorting_helpers.o
	gcc 2.1.o helpers.o sorting_helpers.o -o 2.1.out

2.1.o: 2.1.c 
	gcc -c 2.1.c

helpers.o: helpers.c
	gcc -c helpers.c

sorting_helpers.o: sorting_helpers.c
	gcc -c sorting_helpers.c

clean:
	rm 2.1.o helpers.o sorting_helpers.o