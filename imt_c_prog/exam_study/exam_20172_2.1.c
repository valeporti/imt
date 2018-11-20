#include <stdio.h>
#include <stdlib.h>

float *unit_matrix(int dim)
{
  float *newarray;
  /*** Your code ***/
  //float **matrix;

  newarray = (float**)malloc(sizeof(float*) * dim);
  for (int i = 0; i < dim; i ++) {
    newarray[i] = (float*)malloc(sizeof(float) * dim);
  }

  for (int i = 0; i < dim; i ++) {
    newarray[i][i] = 1;
  }

  //newarray = &matrix;
  
  for (int i = 0; i < 2; i ++) {
    for (int j = 0; j < 2; j ++) {
      //printf("%f ", newarray[i][j]);
    }
    printf("\n");
  }
  

  return newarray;
}

void main() {

  float **arr;

  arr = unit_matrix(2);

  for (int i = 0; i < 2; i ++) {
    for (int j = 0; j < 2; j ++) {
      printf("%f ", arr[i]);
    }
    printf("\n");
  }

}