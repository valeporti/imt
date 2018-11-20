#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void main()
{
  int i, j;
  int arr1[5] = {3, 8, 11, 4, 0}, *arr2;
  char *cstr;
  cstr = (char*)malloc(6*sizeof(char));
  arr2 = arr1 + 3;
  strcpy(cstr, "clock");
  for(j = 0; j<5; j++)
  {
    printf("%c", *cstr);
    cstr++;
  }
  printf("\n");
  for(i = 0; i<5; i++)
  {
    printf("%i ", *arr2);
    arr2++;
  }
}