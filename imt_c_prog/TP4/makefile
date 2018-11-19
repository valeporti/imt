CFLAGS=-DNDEBUG 

all: 2_1 2_1_dbg

# 2_1 for debugging and production
2_1: 2.1.o helpers.o sorting_helpers.o
	gcc 2.1.o helpers.o sorting_helpers.o -o 2.1.out
2.1.o: 2.1.c 
	gcc $(CFLAGS) -c 2.1.c -o 2.1.o

2_1_dbg: 2.1_dbg.o helpers.o sorting_helpers.o
	gcc 2.1_dbg.o helpers.o sorting_helpers.o -o 2.1_dbg.out
2.1_dbg.o: 2.1.c 
	gcc -c 2.1.c -o 2.1_dbg.o

helpers.o: helpers.c
	gcc -c helpers.c

sorting_helpers.o: sorting_helpers.c
	gcc -c sorting_helpers.c

clean:
	rm *.o

clear: 
	rm *.o *.out stocks.txt