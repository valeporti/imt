#include<stdio.h>
#include <stdbool.h> // to be able to use boolean
#include<assert.h> /* BUT https://www.softwariness.com/articles/assertions-in-cpp/ */

#ifdef	NDEBUG
#define assert_condition(x);
#else
#define assert_condition(x) (x) ? printf("Success %s.%i: \u2714\n", __FILE__, __LINE__) : assert(x);
#endif

void main()
{
  // declare variables to read
  int int_type;
  float float_type;
  double double_type;
  short short_type;
  unsigned short u_short_type;
  long long_type;
  bool bool_type;

  // print values
  printf("size of int type %li \n", sizeof(int_type));
  assert_condition(sizeof(int_type) == 4);
  printf("size of float type %li \n", sizeof(float_type));
  assert_condition(sizeof(float_type) == 4);
  printf("size of double type %li \n", sizeof(double_type));
  assert_condition(sizeof(double_type) == 8);
  printf("size of short type %li \n", sizeof(short_type));
  assert_condition(sizeof(short_type) == 2);
  printf("size of unsigned short type %li \n", sizeof(u_short_type));
  assert_condition(sizeof(u_short_type) == 2);
  printf("size of long type %li \n", sizeof(long_type));
  assert_condition(sizeof(long_type) == 8);
  printf("size of boolean type %li \n", sizeof(bool_type));
  assert_condition(sizeof(bool_type) == 1); 
}

