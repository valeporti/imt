#include<stdio.h>
#include <stdbool.h> // to be able to use boolean

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
  printf("size of float type %li \n", sizeof(float_type));
  printf("size of double type %li \n", sizeof(double_type));
  printf("size of short type %li \n", sizeof(short_type));
  printf("size of unsigned short type %li \n", sizeof(u_short_type));
  printf("size of long type %li \n", sizeof(long_type));
  printf("size of boolean type %li \n", sizeof(bool_type));
}

