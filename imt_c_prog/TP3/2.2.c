#include <stdio.h>
#include <stdlib.h>
#include<assert.h>

#ifdef	NDEBUG
#define assert_condition(x, true_msg);
#else
#define assert_condition(x, true_msg) (x) ? printf("Success %s.%i: \u2714 - %s\n", __FILE__, __LINE__, true_msg) : assert(x);
#endif

void main() {

	FILE *bf, *output;
	int num_bytes, num_float_pairs;
	float *x, *y, *floats, *float_read;
	
	assert_condition(1, "START");
	
	bf = fopen("function_data_bin", "r");
	output = fopen("2.2.floats", "w");

	if (bf != NULL) {

		assert_condition(1, "Opened files");
	
		fseek(bf, 0, SEEK_END);
		num_bytes = ftell(bf);
		assert_condition(num_bytes > 0, "bytes in bf file");
		num_float_pairs = num_bytes / (sizeof(float) * 2);
		floats = (float*) malloc(sizeof(float) * num_bytes);
		//printf("file contains bytes: %i\n", num_bytes);
		//printf("file contains x: %i\n", num_float_pairs);

		x = (float*)malloc(sizeof(float) * num_float_pairs);
		y = (float*)malloc(sizeof(float) * num_float_pairs);
		float_read = (float*)malloc(sizeof(float));
		assert_condition(1, "Created x and y arrays and reading pointer array");

		/* read al the file */
		fseek(bf, 0, SEEK_SET); /* put pointer at the begining */
		assert_condition(!ftell(bf), "Reinitialized bf pointer reader");
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
		assert_condition(ftell(bf) == num_bytes, "Ended gathering x and y values");
		
		/* print in file */
		for (int i = 0; i < num_float_pairs; i ++) {
			fprintf(output, "%f %f\n", x[i], y[i]);
		}
		assert_condition(1, "Writen output file");

		fclose(bf);
		fclose(output);
		free(floats);
		free(float_read);
		free(x);
		free(y);
		assert_condition(1, "Closed files and freed arrays' memory");

		system("gnuplot -persist -e 'plot \"2.2.floats\"'");
		assert_condition(1, "Printed on Gnuplot Graph");
	}	
	assert_condition(1, "END");
}
