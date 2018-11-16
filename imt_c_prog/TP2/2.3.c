#include<stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

void changeLettersUpperOrLower (int lower_or_upper, int text_char_counter, char *text);

void main(int argc, char **argv)
{
	char *text;
	int text_char_counter = 0, words_counter = 1, c;
	enum upper_lower {upper, lower};
	enum upper_lower u_l;

	/* ask the user to provide text */
	printf("Hello, please provide text and press enter when finished.\n");
	/* store text in dynamic charachter table */
	text = (char*)malloc(sizeof(char));
	for (;;) {
		//c = fgetc(stdin);
		c = getchar();
		//printf("%i", c);
		text[text_char_counter] = c;
		//printf("%c\n", text[text_char_counter]);
		text_char_counter ++;
		if (c == 10) { break; }
		if (c == 32) { words_counter ++; }
		text = (char*)realloc(text, sizeof(char) * (text_char_counter + 1));
	}
	//printf("text lenght : %i\n", text_char_counter);
	//printf("words : %i\n", words_counter);
	//printf("The text you typed: ");
	for (int i = 0; i < text_char_counter; i ++) {
		printf("%c",text[i]);
	}

	/* to lower or to upper */
	printf("\nPlease type 0 if you want to get your text to upper case or 1 to lower case.\n");
	scanf(" %u", &u_l);
	changeLettersUpperOrLower(u_l, text_char_counter, text);
	printf("\nHere are the words that you gave after changing the case :\n");
	for (int i = 0; i < text_char_counter; i ++) {
		printf("%c",text[i]);
	}

	char *token;
	char **arr_strings;
	char delim[2] = " ";
	int i = 0, j = 0, temp_j = -1, letter_word = 1;

	arr_strings = (char**)malloc(sizeof(char *) * words_counter);

	/* ISSUE ON FREEING: as there is no "\0" assigned, it gets confused */
	/*
	token = strtok(text, delim);
	while( token != NULL ) {
		
		arr_strings[i] = (char*)malloc(sizeof(char) * (strlen(token) + 1));
		printf("\nsize token : %ld", strlen(token));
		arr_strings[i] = strcat(token, "\0");
		printf("\nprint words: %s", token);
		printf("\nprint words: %s", arr_strings[i]);

		i ++;
		token = strtok(NULL, delim);
	}
	*/
	
	int test_counter = 0;
 	for(i = 0;i < text_char_counter; i ++) {

		if (j != temp_j) {
			letter_word = 1;
			arr_strings[j] = (char*)malloc(sizeof(char) * letter_word);
			temp_j = j;
		} else {
			arr_strings[j] = (char*)realloc(arr_strings[j], sizeof(char) * letter_word);
		}

		if (text[i] == 32 ) { 
			arr_strings[j][letter_word] = '\0';
			j++; 
		} else {
			arr_strings[j][letter_word] = text[i];
			letter_word ++;
		}
	}	

	printf("\nTotal of words: %i", words_counter);
	float avg_letter_per_word = ((float)text_char_counter - (float)words_counter) / (float)words_counter;
	printf("\nAverage number of letters per word: %f\n", avg_letter_per_word);

	/* freee mallocs */	
	for (i = 0; i < words_counter; i ++) {
		free(arr_strings[i]);
	}
	free(arr_strings);

	free(text);


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

