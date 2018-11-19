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
	int n;

	if (count_arguments == 2) {
		n = atoi(argv[1]);
	} else {
		printf("please type the dimension 'n' of squared matrix n*n: ");
		scanf(" %i",&n);
		printf("\n");
	}

	assert_condition(n != 0, "N value Captured");
	
	float **matrix;
	int i, j;
	/* Create function filled with zero values */
	
	matrix = (float**)malloc(sizeof(float*) * n); /* Allocate memory for n rows */
	for (i = 0; i < n; i++) {
		matrix[i] = (float*)malloc(sizeof(float) * n); /* Allocate memory for n cols */
		for (j = 0; j < n; j ++) {
			matrix[i][j] = 0;
		}	
	}

	assert_condition(1, "Memory created for 2 dimensional matrix with zeros");

	assign_random_values_to_float_matrix(matrix, n);

	assert_condition(1, "Random variables assigned to squared matrix");

	print_matrix(matrix, n);

	transpose_matrix(matrix, n);

	assert_condition(1, "Transposed Matrix, done");

	printf("\n");
	printf("Transposed matrix\n\n");

	print_matrix(matrix, n);

	/* Free allocated space */
	for (i = 0; i < n; i++) {
		free(matrix[i]);
	}
	free(matrix);

	assert_condition(1, "Freed memory from matrix");
	assert_condition(1, "END");
}