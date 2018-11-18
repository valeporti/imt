#include <stdio.h>

int func(int i)
{
int j = 0;
  do
  {
    printf("j= %i\n", j);
    do  
    {
      int i = 0;
      printf("i= %i\n", i);
      i++;
    }while(i<1);
    j++;
  }while(j<2);
  return i;
}
void main()
{
  printf("Function output = %i\n", func(8));
}