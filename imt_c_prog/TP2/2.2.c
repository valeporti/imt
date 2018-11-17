#include<stdio.h>
#include <stdlib.h>
#include "tp2helpers.h"

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

	assign_random_values_to_float_matrix(matrix, n);

	print_matrix(matrix, n);

	transpose_matrix(matrix, n);

	printf("\n");
	printf("Transposed matrix\n\n");

	print_matrix(matrix, n);

	/* Free allocated space */
	for (i = 0; i < n; i++) {
		free(matrix[i]);
	}
	free(matrix);
}