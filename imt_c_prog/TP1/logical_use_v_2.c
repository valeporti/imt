/* libraries */
#include<stdio.h>
#include"logical.h"
#include<assert.h> /* BUT https://www.softwariness.com/articles/assertions-in-cpp/ */

#ifdef	NDEBUG
#define assert_condition(x, true_msg);
#else
#define assert_condition(x, true_msg) (x) ? printf("Success %s.%i: \u2714 - %s\n", __FILE__, __LINE__, true_msg) : assert(x);
#endif

/* main */
void main()
{

	assert_condition(1, "starting creating the tables");
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
	assert_condition(1, "ended creating the tables");
}


