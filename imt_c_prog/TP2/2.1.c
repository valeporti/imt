#include<stdio.h>
#include <stdlib.h>
#include "tp2helpers.h"
#include<assert.h> /* BUT https://www.softwariness.com/articles/assertions-in-cpp/ */

#ifdef	NDEBUG
#define assert_condition(x, true_msg);
#else
#define assert_condition(x, true_msg) (x) ? printf("Success %s.%i: \u2714 - %s\n", __FILE__, __LINE__, true_msg) : assert(x);
#endif

void main(int argc, char **argv)
{
	int count_arguments = argc; /* 1 for just the program name */
	float a;
	float b;

	assert_condition(1, "started");
	if (count_arguments == 3) {
		a = atof(argv[1]);
		b = atof(argv[2]);
	} else {
		printf("please type the values you want to swap (ex: 5 6): ");
		scanf("%f %f",&a,&b);
		printf("\n");
	}
	assert_condition(1, "Treated the input arguments");
	
	printf(" the value of a and b before swapping %f and %f\n", a, b);
	exchange(&a,&b);
	printf(" the value of a and b afterr swapping %f and %f\n", a, b);

	//assert_condition(1 , "Correct exchange");

	assert_condition(1, "END");
}

