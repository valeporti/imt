#include<stdio.h>

void main() {

	/* AND */
	printf("AND Table \n");

	for (int a = 0; a <= 1; a ++) {
		for (int b = 0; b <= 1; b ++) {
			printf("a %i, b %i AND %i \n", a, b, a && b);
		}
	}
	printf("------------------------------ \n");
	/* OR */
	printf("OR Table \n");
	for (int a = 0; a <= 1; a ++) {
		for (int b = 0; b <= 1; b ++) {
			printf("a %i, b %i OR %i \n", a, b, a || b);
		}
	}
	printf("------------------------------ \n");
	/* XOR */
	printf("XOR Table \n");
	for (int a = 0; a <= 1; a ++) {
		for (int b = 0; b <= 1; b ++) {
			printf("a %i, b %i XOR %i \n", a, b, a ^ b);
		}
	}
}

 


