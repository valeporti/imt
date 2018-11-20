#include<stdio.h>
#include <stdlib.h>
#include <string.h>

struct airplane
{
  char *name;
  int weight;
  unsigned short age;
  float length;
};

int equal_airplanes(struct airplane a1, struct airplane a2) {
  if (!strcmp(a1.name, a2.name) && a1.weight == a2.weight && a1.age == a2.age && a1.length == a2.length) {
    return 1;
  } else {return 0;}
}

void main() {
  struct airplane a1, a2, a3;

  a1.name = (char*)malloc(sizeof(char) * 256);
  strncpy(a1.name,"losasasl", 6);
  a1.weight = 3;
  a1.age = 4;
  a1.length = 4;
  
  
  a2.name = (char*)malloc(sizeof(char) * 26);
  strncpy(a2.name,"lolsadssasa\0", 10);
  a2.weight = 3;
  a2.age = 4;
  a2.length = 4;

  printf("%ld\n", strlen(a2.name));


  
  //if (equal_airplanes(a1, a2)) { printf("equals\n"); } else { printf("equalsNOT\n"); }

  printf("%li\n", sizeof(a3));

  struct airplane planes[2][3];
  int i, j;
  for(i = 0; i<2; i++)
  {
    for(j = 0; j<3; j++)
    {
      printf("%li \n", &(planes[i][j]));
    }
  }
}