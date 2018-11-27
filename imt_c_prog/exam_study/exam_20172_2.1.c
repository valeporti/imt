#include <stdio.h>
#include <stdlib.h>

float *unit_matrix(int dim)
{
  float *newarray;
  /*** Your code ***/
  float **matrix;
  
  newarray = &matrix;

  matrix = (float**)malloc(sizeof(float*) * dim);
  for (int i = 0; i < dim; i ++) {
    matrix[i] = (float*)malloc(sizeof(float) * dim);
  }

  for (int i = 0; i < dim; i ++) {
    matrix[i][i] = 1;
  }

  for (int i = 0; i < 2; i ++) {
    for (int j = 0; j < 2; j ++) {
      printf("%f ", matrix[i][j]);
    }
    printf("\n");
  }
  
  for (int i = 0; i < dim; i ++) {
    free(matrix[i]);
  }

  free(matrix);

  return newarray;
}

void main() {

  float *arr;

  arr = unit_matrix(2);

  for (int i = 0; i < 2; i ++) {
    for (int j = 0; j < 2; j ++) {
      printf("%f ", &(arr[i]));
    }
    printf("\n");
  }

}