#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "tp3helpers.h"

void main(int argc, char **argv) {
	
	int count_arguments = argc;
	float mean, std_dev, samples, sum, *x, *y;
	FILE *output;
	
	if (count_arguments != 4) {
		printf("Sorry, we didn't received the expected number of arguments\n");
		return;
	}

	mean = atof(argv[1]);
	std_dev = atof(argv[2]);
	samples = atoi(argv[3]);

	x = (float*)malloc(sizeof(float) * samples);
	y = (float*)malloc(sizeof(float) * samples);

	calculate_gauss_points(x, y, mean, std_dev, samples);

	/* print values in file */
	output = fopen("2.1.gauss", "w");
	for (int i = 0; i < samples; i ++) {
		fprintf(output, "%f %f\n", x[i], y[i]);
	}
	fclose(output);
	free(x);
	free(y);

	system("gnuplot -persist -e 'plot \"2.1.gauss\" '");
}
