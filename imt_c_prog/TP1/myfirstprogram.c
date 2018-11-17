#include<stdio.h>
#ifdef	NDEBUG
#define assert_condition(x, true_message, false_message);
#else
#define assert_condition(x, true_message, false_message) (x) ? printf("Success %s.%i: %s\n", __FILE__, __LINE__,  true_message) : assert(x && false_message);
#endif
#include<assert.h> /* BUT https://www.softwariness.com/articles/assertions-in-cpp/ */

void main () {

	printf("Hello Valentin PORTILLO\n");
	assert_condition(1, "everything great!", "something happened");
}
