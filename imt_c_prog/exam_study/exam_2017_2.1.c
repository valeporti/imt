#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void print_arr(float an_array[], int n) {
  int i = 0;
  for (i=1; i<=n; i++)
  {
    printf("mem add %li \n", an_array);
    an_array ++ ;
  }
}

void print_char(char an_array[], int n) {
  int i = 0;
  for (i=1; i<=n; i++)
  {
    printf("mem add %s val %c \n", an_array++, *an_array);
    //an_array = an_array + i;
  }
}

void main() {
  float arr[10] = {5,8,3,4,5,6,7,8,9,1}, *arr2;
  arr2 = &arr;
  char *arr1 = (char*)malloc(10);
  strcpy(arr1, "abcdefghi");
  int n = 10;

  for (int i=0; i<n; i++)
  {
    //printf("mem add %p val %c \n", arr1+i, *arr1);
    //an_array = an_array + i;
  }
  for (int i=0; i<n; i++)
  {
    //printf("mem add %li valu %f \n", arr2++, *arr2);
    //an_array = an_array + i;
  }

  print_arr(arr, n);
  //print_char(arr1,n);
}