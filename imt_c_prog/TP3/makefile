CFLAGS=-DNDEBUG 

all: 2_1 2_2 2_3 2_1_dbg 2_2_dbg 2_3_dbg 

#2_3 debbuging and production files
2_3: 2.3.o tp3helpers.o
	gcc -o 2.3.out 2.3.o tp3helpers.o -lm 
2.3.o: 2.3.c
	gcc $(CFLAGS) -c 2.3.c -o 2.3.o

2_3_dbg: 2.3_dbg.o tp3helpers_dbg.o
	gcc -o 2.3_dbg.out 2.3_dbg.o tp3helpers_dbg.o -lm 
2.3_dbg.o: 2.3.c
	gcc -c 2.3.c -o 2.3_dbg.o

#2_2 debbuging and production files
2_2: 2.2.o
	gcc -o 2.2.out 2.2.o
2.2.o: 2.2.c
	gcc $(CFLAGS) -c 2.2.c -o 2.2.o

2_2_dbg: 2.2_dbg.o
	gcc -o 2.2_dbg.out 2.2_dbg.o
2.2_dbg.o: 2.2.c
	gcc -c 2.2.c -o 2.2_dbg.o

#2_1 debbuging and production files
2_1: 2.1.o tp3helpers.o
	gcc -o 2.1.out 2.1.o tp3helpers.o -lm 
2.1.o: 2.1.c 
	gcc $(CFLAGS) -c 2.1.c -o 2.1.o

2_1_dbg: 2.1_dbg.o tp3helpers.o
	gcc -o 2.1_dbg.out 2.1_dbg.o tp3helpers.o -lm 
2.1_dbg.o: 2.1.c 
	gcc -c 2.1.c -o 2.1_dbg.o

#tp3 debugg and production files
tp3helpers.o: tp3helpers.c
	gcc $(CFLAGS) -c tp3helpers.c -o tp3helpers.o
tp3helpers_dbg.o: tp3helpers.c
	gcc -c tp3helpers.c -o tp3helpers_dbg.o

clean:
	rm *.o 

clear: 
	rm *.o *.out *.gauss *.floats compressed.bin -rf unpacked