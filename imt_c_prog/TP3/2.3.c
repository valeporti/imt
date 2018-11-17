#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "tp3helpers.h"

void main(int argc, char **argv) {

	if (argc == 1) {
		printf("Program usage is as follows.\n");
		printf("For compressing a file type: ./2.3.out -c file_to_compress_1 file_to_compress_3 ...\n");
		printf("For decompressing a file type: ./2.3.out -d file_to_decompress\n");
		/* ask for arguments, show example */
		return;
	}

	/* open file, overwrite it if existant in order to pack */
	char **array_of_names;
	char *pack_unpack_file_name = argv[2];

	if ( !strcmp(argv[1], "-c") ) {		
		array_of_names = argv + 2;
		file_packing("compressed.bin", argc - 2, array_of_names);
	}
	else if ( !strcmp(argv[1], "-d") ) {
		file_unpacking(pack_unpack_file_name);
	} 
	else {
		/* mark not expected arguments, or missing, send same message of usage */
		printf("Program usage is as follows.\n");
		printf("For compressing a file type: ./2.3.out -c file_to_compress_1 file_to_compress_3 ...\n");
		printf("For decompressing a file type: ./2.3.out -d file_to_decompress\n");
	}	
}

/*
	printf("%s\n", array_of_names[i]);
		printf("%s\n", to_pck_stct.filename);
		printf("%d\n", to_pck_stct.num_of_bytes);
		//printf("is it");
		//fflush(stdin);
*/