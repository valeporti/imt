#include <stdio.h>
#include <stdlib.h>

void main() {

	FILE *bf, *output;
	int num_bytes, num_float_pairs;
	float *x, *y, *floats, *float_read;
	
	
	bf = fopen("function_data_bin", "r");
	output = fopen("2.2.floats", "w");

	if (bf != NULL) {
	
		fseek(bf, 0, SEEK_END);
		num_bytes = ftell(bf);
		num_float_pairs = num_bytes / (sizeof(float) * 2);
		floats = (float*) malloc(sizeof(float) * num_bytes);
		printf("file contains bytes: %i\n", num_bytes);
		printf("file contains x: %i\n", num_float_pairs);

		x = (float*)malloc(sizeof(float) * num_float_pairs);
		y = (float*)malloc(sizeof(float) * num_float_pairs);
		float_read = (float*)malloc(sizeof(float));

		/* read al the file */
		fseek(bf, 0, SEEK_SET); /* put pointer at the begining */
		/* read the x floats */
		for (int i = 0; i < num_float_pairs; i ++) {
			fread(float_read, sizeof(float), 1, bf);
			x[i] = *float_read;
			//printf("%f\n", *float_read);
		}
		for (int i = 0; i < num_float_pairs; i ++) {
			fread(float_read, sizeof(float), 1, bf);
			y[i] = *float_read;
			//printf("%f\n", *float_read);
		}
		
		/* print in file */
		for (int i = 0; i < num_float_pairs; i ++) {
			fprintf(output, "%f %f\n", x[i], y[i]);
		}

		fclose(bf);
		fclose(output);
		free(x);
		free(y);

		system("gnuplot -persist -e 'plot \"2.2.floats\"'");
	}	
}
