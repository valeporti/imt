#include <stdio.h>
#include <stdlib.h>

void main() {

	FILE *bf;
  int num_bytes;
	
	bf = fopen("txt.txt", "r");

	if (bf != NULL) {


		fseek(bf, 0, SEEK_END);
		num_bytes = ftell(bf);
    printf("%i\n", num_bytes);
  }
}