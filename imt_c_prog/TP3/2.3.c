#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_FNAME_LENGTH 256

struct filestructure
{
	char filename[MAX_FNAME_LENGTH];
	unsigned int num_of_bytes; /* size: 4 bytes */
};
typedef struct filestructure filestruct;

void file_packing(char *packed_file_name, int num_of_files, char **array_of_names);
void file_unpacking(char *packed_file_name);

void main(int argc, char **argv) {

	if (argc == 1) {
		
		/* ask for arguments, show example */
		return;
	}

	/* open file, overwrite it if existant in order to pack */
	char **array_of_names;
	char *pack_unpack_file_name = "test_pack.bin";

	if ( !strcmp(argv[1], "-c") ) {		
		array_of_names = argv + 2;
		file_packing(pack_unpack_file_name, argc - 2, array_of_names);
	}
	else if ( !strcmp(argv[1], "-d") ) {
		file_unpacking(pack_unpack_file_name);
	} 
	else {
		/* mark not expected arguments, or missing, send same message of usage */
	}	
}

void file_packing(char *packed_file_name, int num_of_files, char **array_of_names) {

	FILE *to_pck, *pck;
	filestruct to_pck_stct; 
	char byte_to_write[1];
	
	pck = fopen(packed_file_name, "w");

	for (int i = 0; i < num_of_files; i ++) {
		
		/* try to open */
		to_pck = fopen(array_of_names[i], "r");
		if (to_pck == NULL) { continue; }

		/* Search info */
		fseek(to_pck, 0, SEEK_END);
		to_pck_stct.num_of_bytes = ftell(to_pck);
		strncpy(to_pck_stct.filename, array_of_names[i], strlen(array_of_names[i]));
		to_pck_stct.filename[strlen(array_of_names[i])] = '\0'; /* add the ending of string character */
		/* restore file pointer */
		fseek(to_pck, 0, SEEK_SET);

		/* prepare the packing / unpacking file to receive new bytes */
		fwrite((const void*) &to_pck_stct.num_of_bytes, sizeof(to_pck_stct.num_of_bytes), 1, pck);
		fwrite((const void*) &to_pck_stct.filename, sizeof(to_pck_stct.filename), 1, pck);

		/* Read Through content and copy it to main file */
		for (int c = 0; c < to_pck_stct.num_of_bytes; c ++) {
			fread(&byte_to_write, sizeof(char), 1, to_pck);
			fwrite((const void*) &byte_to_write, sizeof(unsigned char), 1, pck);
		}
		
		fclose(to_pck);
	}

	fclose(pck);
  
}

void file_unpacking(char *packed_file_name) {

	FILE *pck, *unpck;
	filestruct to_unpck_stct; 
	char byte_to_read[1], new_dir[256];
	unsigned int total_bytes = 0, i, c, file_counter = 1;

	pck = fopen(packed_file_name, "r");

	if (pck == NULL) { printf("issue op"); return; }

	fseek(pck, 0, SEEK_END);
	total_bytes = ftell(pck);
	//if (total_bytes < sizeof(to_unpck_stct.num_of_bytes) + sizeof(to_unpck_stct.filename)) { return; }
	fseek(pck, 0, SEEK_SET);

	system("mkdir ./unpacked");

	for (i = 0; i < total_bytes; i ++) {

		fread(&to_unpck_stct.num_of_bytes, sizeof(to_unpck_stct.num_of_bytes), 1, pck);
		fread(&to_unpck_stct.filename, sizeof(to_unpck_stct.filename), 1, pck);

		printf("\n%i.- Unpacked %s file with %i bytes", file_counter, to_unpck_stct.filename, to_unpck_stct.num_of_bytes);
		
		/* Pen new file */
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
	printf("\n");
	fclose(pck);
}

/*
	printf("%s\n", array_of_names[i]);
		printf("%s\n", to_pck_stct.filename);
		printf("%d\n", to_pck_stct.num_of_bytes);
		//printf("is it");
		//fflush(stdin);
*/