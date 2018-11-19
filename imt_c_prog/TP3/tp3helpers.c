#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<assert.h>

#ifdef	NDEBUG
#define assert_condition(x, true_msg);
#else
#define assert_condition(x, true_msg) (x) ? printf("Success %s.%i: \u2714 - %s\n", __FILE__, __LINE__, true_msg) : assert(x);
#endif

#define MAX_FNAME_LENGTH 256

struct filestructure
{
	char filename[MAX_FNAME_LENGTH];
	unsigned int num_of_bytes; /* size: 4 bytes */
};
typedef struct filestructure filestruct;

void calculate_gauss_points(float *x, float *y, float mean, float std_dev, float samples) {
	float min, max, step, cum_step, first, second;

	step = (mean * std_dev * 2) / (float)samples;
	min = mean - mean * std_dev;
	cum_step = min;
	//printf("steps %f\n", step);
	
	first = (1 / (std_dev * sqrt(2 * M_PI)));
	
	//printf("first: %f\n", first);
	for (int i = 0; i < samples; i ++) {
		x[i] = cum_step + step;
		second = exp(-pow(x[i] - mean, 2) / (2 * std_dev * std_dev));
		//printf("second: %f\n", second);
		y[i] =  first * second;
		cum_step += step;
	}
}

void file_packing(char *packed_file_name, int num_of_files, char **array_of_names) {

	FILE *to_pck, *pck;
	filestruct to_pck_stct; 
	char byte_to_write[1];
  int file_counter = 1;

	pck = fopen(packed_file_name, "w");
  printf("\n Compressing/Packing...\n");

	for (int i = 0; i < num_of_files; i ++) {
		
		/* try to open */
		to_pck = fopen(array_of_names[i], "r");
		if (to_pck == NULL) { continue; }
		assert_condition(1, "Opened File to compress");

		/* Search info */
		fseek(to_pck, 0, SEEK_END);
		assert_condition(ftell(to_pck), "Read bytes / Non empty to pack file");
		to_pck_stct.num_of_bytes = ftell(to_pck);
		strncpy(to_pck_stct.filename, array_of_names[i], strlen(array_of_names[i]));
		to_pck_stct.filename[strlen(array_of_names[i])] = '\0'; /* add the ending of string character */
		/* restore file pointer */
		fseek(to_pck, 0, SEEK_SET);
		assert_condition(!ftell(to_pck), "Reinitialized pointer on to_pack file");

		/* prepare the packing / unpacking file to receive new bytes */
		fwrite((const void*) &to_pck_stct.num_of_bytes, sizeof(to_pck_stct.num_of_bytes), 1, pck);
		fwrite((const void*) &to_pck_stct.filename, sizeof(to_pck_stct.filename), 1, pck);
		assert_condition(1, "Writen titles on destiny file");

		/* Read Through content and copy it to main file */
		for (int c = 0; c < to_pck_stct.num_of_bytes; c ++) {
			fread(&byte_to_write, sizeof(char), 1, to_pck);
			fwrite((const void*) &byte_to_write, sizeof(unsigned char), 1, pck);
		}
		assert_condition(1, "Ended passing each byte to destiny file");

    printf("%i.- Packed %s file with %i bytes\n", file_counter ++, to_pck_stct.filename, to_pck_stct.num_of_bytes);
		
		fclose(to_pck);
	}

	fclose(pck);
	assert_condition(1, "Closed all used files");
  
}

void file_unpacking(char *packed_file_name) {

	FILE *pck, *unpck;
	filestruct to_unpck_stct; 
	char byte_to_read[1], new_dir[256];
	unsigned int total_bytes = 0, i, c, file_counter = 1;

	pck = fopen(packed_file_name, "r");

	if (pck == NULL) { printf("issue op"); return; }
	assert_condition(1, "Opened File to uncompress");
  printf("\n Unpacking/Uncompressing...\n");

	fseek(pck, 0, SEEK_END);
	assert_condition(ftell(pck), "Read bytes / Non empty pack file");
	total_bytes = ftell(pck);
	//if (total_bytes < sizeof(to_unpck_stct.num_of_bytes) + sizeof(to_unpck_stct.filename)) { return; }
	fseek(pck, 0, SEEK_SET);
	assert_condition(!ftell(pck), "Reinitialized pointer on pack file");
	
	system("mkdir ./unpacked"); /* new directory, where to store unpacked files */
	assert_condition(1, "Created or Already existant directory");

	for (i = 0; i < total_bytes; i ++) {

		fread(&to_unpck_stct.num_of_bytes, sizeof(to_unpck_stct.num_of_bytes), 1, pck);
		fread(&to_unpck_stct.filename, sizeof(to_unpck_stct.filename), 1, pck);

		printf("\n%i.- Unpacked %s file with %i bytes", file_counter, to_unpck_stct.filename, to_unpck_stct.num_of_bytes);
		
		/* Open new file */
		strcpy(new_dir, "./unpacked/");
		strcat(new_dir, to_unpck_stct.filename);
		unpck = fopen(new_dir, "w");
		
		/* Read Through content and copy it to new file */
		for (c = 0; c < to_unpck_stct.num_of_bytes; c ++) {
			fread(byte_to_read, sizeof(char), 1, pck);
			fwrite(byte_to_read, sizeof(char), 1, unpck);
		}
		
		fclose(unpck);
		i += c + sizeof(to_unpck_stct.num_of_bytes) + sizeof(to_unpck_stct.filename);
		file_counter ++;
	}
	assert_condition(1, "Ended unpacking");
	printf("\n");
	fclose(pck);
	assert_condition(1, "Closed all used files");
}
