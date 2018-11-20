#include <stdio.h>

void main() {
  float data=2.5;
  data += 1.5;
  data -= 1.5;
  if(data == 2.5)
  {
    printf("True\n");
    printf("%f\n", data * 10000000);
  }
  else
  {
    printf("False\n");
  }
}