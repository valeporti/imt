#include<stdio.h>

void print_arr(float an_array[], int n) {
  int i = 0;
  for (i=1; i<=n+4; i++)
  {
    printf("%f \n", *an_array);
    an_array++;
  }
}

void main() {
  float arr[10] = {1,2,3,4,5,6,7,8,9,1};
  int n = 10;

  print_arr(arr, n);
}