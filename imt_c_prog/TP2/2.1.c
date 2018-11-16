#include<stdio.h>
#include <stdlib.h>

void exchange(float *x, float *y);

void main(int argc, char **argv)
{


	int count_arguments = argc; /* 1 for just the program name */
	float a;
	float b;

	if (count_arguments == 3) {
		a = atof(argv[1]);
		b = atof(argv[2]);
	} else {
		printf("please type the values you want to swap (ex: 5 6): ");
		scanf("%f %f",&a,&b);
		printf("\n");
	}
	
	printf(" the value of a and b before swapping %f and %f\n", a, b);
	exchange(&a,&b);
	printf(" the value of a and b afterr swapping %f and %f\n", a, b);

}
 
void exchange (float *x, float *y)
{
	float temp; /* = null */

	temp = *x; /* dont loose x */
	*x = *y; /* assign y */
	*y = temp; /* get temp value */
}

