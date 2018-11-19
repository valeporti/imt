#include<stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "tp2helpers.h"
#include<assert.h>

#ifdef	NDEBUG
#define assert_condition(x, true_msg);
#else
#define assert_condition(x, true_msg) (x) ? printf("Success %s.%i: \u2714 - %s\n", __FILE__, __LINE__, true_msg) : assert(x);
#endif

void main(int argc, char **argv)
{
	char *text;
	int text_char_counter = 0, words_counter = 1, c;
	enum upper_lower {upper, lower};
	enum upper_lower u_l;

	assert_condition(1, "Started Progam");

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
	assert_condition(1, "Text in array");
	//printf("text lenght : %i\n", text_char_counter);
	//printf("words : %i\n", words_counter);
	//printf("The text you typed: ");
	for (int i = 0; i < text_char_counter; i ++) {
		printf("%c",text[i]);
	}

	/* to lower or to upper */
	printf("\nPlease type 0 if you want to get your text to upper case or 1 to lower case.\n");
	scanf(" %u", &u_l);
	assert_condition(u_l >= 0, "Got Upper OR Lower variable");
	changeLettersUpperOrLower(u_l, text_char_counter, text);
	assert_condition(1, "Done lower or Upper function");
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
	assert_condition(1, "Rearanged matrix on a tree of words");

	printf("\nTotal of words: %i", words_counter);
	float avg_letter_per_word = ((float)text_char_counter - (float)words_counter) / (float)words_counter;
	printf("\nAverage number of letters per word: %f\n", avg_letter_per_word);

	/* freee mallocs */	
	for (i = 0; i < words_counter; i ++) {
		free(arr_strings[i]);
	}
	free(arr_strings);
	assert_condition(1, "Freed memory from matrix");

	free(text);

	assert_condition(1, "Freed memory of text");
	assert_condition(1, "END");
}

