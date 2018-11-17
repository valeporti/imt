/* libraries */
#include<stdio.h>
#include <ctype.h>

/* main */
void main() {
    int characters_to_print = 130; /* 94 printable characters */
    printf("\nWe'll print here every possible printable character and its corresponding integer\n");
    for (int i = 0; i < characters_to_print; i ++) {
        printf("%i || ", i);
        if (isprint(i)) {
            putchar(i);
        }  
        printf("\n");
    } 
}