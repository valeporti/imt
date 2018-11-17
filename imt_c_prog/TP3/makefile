all: 2_1 2_2 2_3

2_3: 2.3.o tp3helpers.o
	gcc -o 2.3.out 2.3.o tp3helpers.o -lm 

2.3.o: 2.3.c
	gcc -c 2.3.c

2_2: 2.2.o
	gcc -o 2.2.out 2.2.o

2.2.o: 2.2.c
	gcc -c 2.2.c

2_1: 2.1.o tp3helpers.o
	gcc -o 2.1.out 2.1.o tp3helpers.o -lm 
	
2.1.o: 2.1.c 
	gcc -c 2.1.c

tp3helpers.o: tp3helpers.c
	gcc -c tp3helpers.c

clean:
	rm *.o 