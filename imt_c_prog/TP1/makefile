CFLAGS=-DNDEBUG 

all: myfirstprogram myfirstprogram_dbg 2_2 logical_use_v_1 logical_use_v_1_dbg logical_use_v_2 logical_use_v_2_dbg 2_4_1 2_4_1_dbg 2_4_2 2_4_2_dbg 2_2_dbg

# 2.4.2 debugging and production files
2_4_2: 2.4.2.o conv_helpers.o
	gcc -o 2.4.2.out 2.4.2.o conv_helpers.o
2.4.2.o: 2.4.2.c
	gcc $(CFLAGS) -c 2.4.2.c -o 2.4.2.o
conv_helpers.o: conv_helpers.c
	gcc $(CFLAGS) -c conv_helpers.c -o conv_helpers.o

2.4.2_dbg.o: 2.4.2.c
	gcc -c 2.4.2.c -o 2.4.2_dbg.o
conv_helpers_dbg.o: conv_helpers.c
	gcc -c conv_helpers.c -o conv_helpers_dbg.o
2_4_2_dbg: 2.4.2_dbg.o conv_helpers_dbg.o
	gcc -o 2.4.2_dbg.out 2.4.2_dbg.o conv_helpers_dbg.o

# 2.4.1 debugging and production files
2_4_1_dbg: 2.4.1_dbg.o
	gcc -o 2.4.1_dbg.out 2.4.1_dbg.o
2.4.1_dbg.o: 2.4.1.c 
	gcc -c 2.4.1.c -o 2.4.1_dbg.o

2_4_1: 2.4.1.o
	gcc -o 2.4.1.out 2.4.1.o
2.4.1.o: 2.4.1.c
	gcc $(CFLAGS) -c 2.4.1.c -o 2.4.1.o

# logical use debugging and production files
logical_use_v_2: logical_use_v_2.o logical.o
	gcc -o logical_use_v_2.out logical_use_v_2.o logical.o
logical_use_v_2.o: logical_use_v_2.c
	gcc $(CFLAGS) -c logical_use_v_2.c -o logical_use_v_2.o
logical.o: logical.c
	gcc $(CFLAGS) -c logical.c -o logical.o

logical_use_v_2_dbg: logical_use_v_2_dbg.o logical_dbg.o
	gcc -o logical_use_v_2_dbg.out logical_use_v_2_dbg.o logical_dbg.o
logical_use_v_2_dbg.o: logical_use_v_2.c
	gcc -c logical_use_v_2.c -o logical_use_v_2_dbg.o
logical_dbg.o: logical.c
	gcc -c logical.c -o logical_dbg.o

# logical use V1 debugging and production files
logical_use_v_1: logical_use_v_1.o
	gcc -o logical_use_v_1.out logical_use_v_1.o
logical_use_v_1.o: logical_use_v_1.c
	gcc $(CFLAGS) -c logical_use_v_1.c -logical_use_v_1.o

logical_use_v_1_dbg: logical_use_v_1_dbg.o
	gcc -o logical_use_v_1_dbg.out logical_use_v_1_dbg.o
logical_use_v_1_dbg.o: logical_use_v_1.c
	gcc -c logical_use_v_1.c -o logical_use_v_1_dbg.o

# 2.2 debugging and production files
2_2_dbg: 2.2_dbg.o
	gcc -o 2.2_dbg.out 2.2_dbg.o
2.2_dbg.o: 2.2.c
	gcc -c 2.2.c -o 2.2_dbg.o

2_2: 2.2.o
	gcc -o 2.2.out 2.2.o
2.2.o: 2.2.c
	gcc $(CFLAGS) -c 2.2.c -o 2.2.o

# my first program debugging and production files
myfirstprogram_dbg: myfirstprogram_dbg.o
	gcc -o myprog_dbg.hello myfirstprogram_dbg.o
myfirstprogram_dbg.o: myfirstprogram.c
	gcc -c myfirstprogram.c -o myfirstprogram_dbg.o

myfirstprogram: myfirstprogram.o
	gcc -o myprog.hello myfirstprogram.o
myfirstprogram.o: myfirstprogram.c
	gcc $(CFLAGS) -c myfirstprogram.c -o myfirstprogram.o

clean: 
	rm *.o