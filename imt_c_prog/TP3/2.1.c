#include <stdio.h>
#include <math.h>
#include <stdlib.h>

void main(int argc, char **argv) {
	
	int count_arguments = argc;
	float mean, std_dev, samples, sum, *x, *y, min, max;
	
	if (count_arguments != 4) {
		printf("Sorry, we didn't received the expected number of arguments\n");
		return;
	}

	mean = atof(argv[1]);
	std_dev = atof(argv[2]);
	samples = atoi(argv[3]);

	x = (float*)malloc(sizeof(float) * samples);
	y = (float*)malloc(sizeof(float) * samples);

	/* calculate standard dev */
	/* https://ncalculators.com/statistics/normal-distribution-calculator.htm */
	float step, cum_step, first, second;

	
	step = (mean * std_dev * 2) / (float)samples;
	min = mean - mean * std_dev;
	cum_step = min;
	printf("steps %f\n", step);
	
	first = (1 / (std_dev * sqrt(2 * M_PI)));
	
	printf("first: %f\n", first);
	for (int i = 0; i < samples; i ++) {
		x[i] = cum_step + step;
		second = exp(-pow(x[i] - mean, 2) / (2 * std_dev * std_dev));
		printf("second: %f\n", second);
		y[i] =  first * second;
		cum_step += step;
	}

	/* print values in file */
	FILE *output;
	output = fopen("2.1.gauss", "w");
	for (int i = 0; i < samples; i ++) {
		fprintf(output, "%f %f\n", x[i], y[i]);
	}
	fclose(output);
	free(x);
	free(y);

	system("gnuplot -persist -e 'plot \"2.1.gauss\" '");
}
