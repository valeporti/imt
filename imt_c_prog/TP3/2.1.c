#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "tp3helpers.h"
#include<assert.h>

#ifdef	NDEBUG
#define assert_condition(x, true_msg);
#else
#define assert_condition(x, true_msg) (x) ? printf("Success %s.%i: \u2714 - %s\n", __FILE__, __LINE__, true_msg) : assert(x);
#endif

void main(int argc, char **argv) {
	
	int count_arguments = argc;
	float mean, std_dev, samples, sum, *x, *y;
	FILE *output;

	assert_condition(1, "Start Program");
	
	if (count_arguments != 4) {
		printf("Sorry, we didn't received the expected number of arguments\nProgram Usage: ./2.1.out mean standard_deviation #_samples\nfor example: ./2.1.out 3 0.6 20");
		return;
	}

	mean = atof(argv[1]);
	std_dev = atof(argv[2]);
	samples = atoi(argv[3]);

	x = (float*)malloc(sizeof(float) * samples);
	y = (float*)malloc(sizeof(float) * samples);

	assert_condition(1, "Initialized variables from arguments and arrays of values");

	calculate_gauss_points(x, y, mean, std_dev, samples);

	assert_condition(1, "Calculated Gauss Points");

	/* print values in file */
	output = fopen("2.1.gauss", "w");
	for (int i = 0; i < samples; i ++) {
		fprintf(output, "%f %f\n", x[i], y[i]);
	}

	fclose(output);
	free(x);
	free(y);
	assert_condition(1, "Closed files and freed arrays' memory");

	system("gnuplot -persist -e 'plot \"2.1.gauss\" '");

	assert_condition(1, "Printed on Gnuplot Graph");
	assert_condition(1, "End");
}
