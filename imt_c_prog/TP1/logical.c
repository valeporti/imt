#include<stdio.h>

/* functions */
void logical_operator_use(char x)
{
	for (int a = 0; a <= 1; a ++) {
		for (int b = 0; b <= 1; b ++) {
			int operation;
			switch (x) {
				case 'A':
				{
					operation = a && b;
					printf("a %i, b %i %s %i \n", a, b, "AND", operation);
					break;
				}
				case 'O':
				{       operation = a || b;
					printf("a %i, b %i %s %i \n", a, b, "OR", operation);
					break;
				}
				case 'X':
				{       operation = a ^ b;
					printf("a %i, b %i %s %i \n", a, b, "xor", operation);
					break;
				}
			}
			
		}
	}
}
