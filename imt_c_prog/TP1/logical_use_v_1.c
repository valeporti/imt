#include<stdio.h>
#include<assert.h> /* BUT https://www.softwariness.com/articles/assertions-in-cpp/ */

#ifdef	NDEBUG
#define assert_condition(x, true_msg);
#else
#define assert_condition(x, true_msg) (x) ? printf("Success %s.%i: \u2714 - %s\n", __FILE__, __LINE__, true_msg) : assert(x);
#endif

void main() {

	assert_condition(1, "starting creating the tables");

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

	assert_condition(1, "ended creating the tables");
}

 


