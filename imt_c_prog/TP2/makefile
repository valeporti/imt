all: 2_1 2_2

2_2: 2.2.o tp2helpers.o
	gcc -o 2.2.out 2.2.o tp2helpers.o

2.2.o: 2.2.c
	gcc -c 2.2.c

2_1: 2.1.o tp2helpers.o
	gcc -o 2.1.out 2.1.o tp2helpers.o

2.1.o: 2.1.c
	gcc -c 2.1.c

tp2helpers.o: tp2helpers.c
	gcc -c tp2helpers.c

clean: 
	rm tp2helpers.o 2.1.o 2.2.o 2.3.o