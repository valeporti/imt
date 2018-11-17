#include<stdio.h>
#include<assert.h> /* BUT https://www.softwariness.com/articles/assertions-in-cpp/ */

#ifdef	NDEBUG
#define assert_condition(x, true_msg);
#else
#define assert_condition(x, true_msg) (x) ? printf("Success %s.%i: \u2714 - %s\n", __FILE__, __LINE__, true_msg) : assert(x);
#endif

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
