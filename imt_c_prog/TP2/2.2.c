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

	/* Assign random values to the matrix rand() % 50 */
	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j ++) {
			matrix[i][j] = (float)rand()/(float)(RAND_MAX/10); /* https://stackoverflow.com/questions/13408990/how-to-generate-random-float-number-in-c */
			printf("%f ", matrix[i][j]);
		}	
		printf("\n");
	}

	/* Transpose */
	for (i = 0; i < n; i++) {
		for (j = i + 1; j < n; j ++) {
			exchange(&matrix[i][j], &matrix[j][i]);
		}	
	}

	printf("\n");
	printf("Transposed matrix\n\n");

	/* Just print final values */
	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j ++) {
			printf("%f ", matrix[i][j]);
		}	
		printf("\n");
	}

	/* Free allocated space */
	for (i = 0; i < n; i++) {
		free(matrix[i]);
	}
	free(matrix);
}
