#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void initializeStr(char *str, int n) {
  for (int i = 0; i < n; i ++) {
    str[i] = 0;
  }
}

void getStr(char *from_str, char *to_str, int from, int n) {
  int i, c = 0;
  for (i = 0; i < n; i ++) {
    if (!c && (from_str[from + i] == 10 || from_str[from + i] == 127 || from_str[from + i] == 32)) { continue; }
    to_str[c] = from_str[from + i];
    c ++;
    //printf("c:%i ", from_str[from + i]);
  }
  to_str[i ++] = '\0';
}

void removeSpaces(char *str) {
  int c = 0, d = 0;
  char blank[256];

  while (str[c] != '\0') {
    printf("c: %i", str[c]);
    if (str[c] == ' ' || str[c] <= 32 || str[c] == 127) {
        int temp = c + 1;
        if (str[temp] != '\0') {
          while (str[temp] == ' ' && str[temp] != '\0') {
              if (str[temp] == ' ') {
                c++;
              }  
              temp++;
          }
        }
    }
    blank[d] = str[c];
    c++;
    d++;
  }
  blank[d] = '\0';
  strcpy(str, blank);
}