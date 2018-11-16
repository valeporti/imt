/* libraries */
#include<stdio.h>
#include"logical.h"

/* main */
void main()
{

	/* AND */
	printf("\nAND Table \n");
	logical_operator_use('A');
	printf("------------------------------ \n");
	/* OR */
	printf("OR Table \n");
	logical_operator_use('O');
	printf("------------------------------ \n");
	/* XOR */
	printf("XOR Table \n");
	logical_operator_use('X');
}


