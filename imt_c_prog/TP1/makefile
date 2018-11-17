all: myfirstprogram 2_2 logical_use_v_1 logical_use_v_2 2_4_1 2_4_2

2_4_2: 2.4.2.o conv_helpers.o
	gcc -o 2.4.2.out 2.4.2.o conv_helpers.o

2.4.2.o: 2.4.2.c
	gcc -c 2.4.2.c

conv_helpers.o: conv_helpers.c
	gcc -c conv_helpers.c

2_4_1: 2.4.1.o
	gcc -o 2.4.1.out 2.4.1.o

2.4.1.o: 2.4.1.c
	gcc -c 2.4.1.c

logical_use_v_2: logical_use_v_2.o logical.o
	gcc -o logical_use_v_2.out logical_use_v_2.o logical.o

logical_use_v_2.o: logical_use_v_2.c
	gcc -c logical_use_v_2.c

logical.o: logical.c
	gcc -c logical.c

logical_use_v_1: logical_use_v_1.o
	gcc -o logical_use_v_1.out logical_use_v_1.o

logical_use_v_1.o: logical_use_v_1.c
	gcc -c logical_use_v_1.c

2_2: 2.2.o
	gcc -o 2.2.out 2.2.o

2.2.o: 2.2.c
	gcc -c 2.2.c

myfirstprogram: myfirstprogram.o
	gcc -o myprog.hello myfirstprogram.o

myfirstprogram.o: myfirstprogram.c
	gcc -c myfirstprogram.c

clean: 
	rm myfirstprogram.o 2.2.o logical_use_v_1.o logical.o logical_use_v_2.o conv_helpers.o 2.4.1.o 2.4.2.o