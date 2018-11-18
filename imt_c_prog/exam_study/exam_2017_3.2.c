#include<stdio.h>

#define mypi1 3.14

void main() {
  float mypi2 = 3.14;
  long mypi3 = 3.14;
  printf("%i \n", mypi1 == mypi2);
  printf("%f \n", (double)mypi2 * 10000);
  printf("%f \n", mypi1 * 10000);
  printf("%li \n", sizeof(mypi1));
  printf("%li \n", sizeof(mypi2));
  printf("%i \n", mypi1 == mypi3);
  printf("%li \n", sizeof(mypi3));

 
}