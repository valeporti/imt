/* libraries */
#include<stdio.h>
#include <ctype.h>
#include<assert.h> /* BUT https://www.softwariness.com/articles/assertions-in-cpp/ */

#ifdef	NDEBUG
#define assert_condition(x);
#else
#define assert_condition(x) (x) ? printf("Success %s.%i: \u2714\n", __FILE__, __LINE__) : assert(x);
#endif

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
    assert_condition(1);
}