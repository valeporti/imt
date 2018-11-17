#include<stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

void exchange (float *x, float *y)
{
	float temp; /* = null */

	temp = *x; /* dont loose x */
	*x = *y; /* assign y */
	*y = temp; /* get temp value */
}

void assign_random_values_to_float_matrix(float **matrix, int n) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j ++) {
			matrix[i][j] = (float)rand()/(float)(RAND_MAX/10); /* https://stackoverflow.com/questions/13408990/how-to-generate-random-float-number-in-c */
		}	
	}
}

void transpose_matrix(float **matrix, int n) {
	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j ++) {
			exchange(&matrix[i][j], &matrix[j][i]);
		}	
	}
}

void print_matrix(float **matrix, int n) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j ++) {
			printf("%f ", matrix[i][j]);
		}	
		printf("\n");
	}
}

void changeLettersUpperOrLower (int lower_or_upper, int text_char_counter, char *text) {

	for (int i = 0; i < text_char_counter - 1; i ++) {
		if (lower_or_upper == 0) {
			text[i] = toupper(text[i]);
		} else {
			text[i] = tolower(text[i]);
		}
	}
}