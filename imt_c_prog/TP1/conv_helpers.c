#include<stdio.h>
#include <ctype.h>
#include <string.h>

int isValueInArray(char arr[], int size_av_tr, char searched_char);

char * get_value_form_char(char letter) {
  switch (toupper(letter)) 
  {
    case 'E':
    {
      return "\u20AC";
      break;
    }
    case 'U':
    {
      return "\u0024";
      break;
    }
    case 'P':
    {
      return "\u00A3";
      break;
    }
    default: 
    {
      return " ";
    }
  }
}

float get_corresponding_ratio(char available_trades[], int size_av_tr, float trade_values[], char from, char to, char pivot) {
  
  int acc = 10000;
  char to_upper_from = toupper(from);
  char to_upper_to = toupper(to);
  char to_upper_pivot = toupper(pivot);
  
  if (to_upper_from == to_upper_to) {
    return 1;
  } 
  else if (to_upper_from == to_upper_pivot) {
    //printf("ok, pasa por aqui");
    int index = isValueInArray(available_trades, size_av_tr, to_upper_to);
    //printf("\nmuestra index %i\n", index);
    if (index < 0) { return 0; }
    return trade_values[index];
  }
  else if (to_upper_to == to_upper_pivot) {
    //printf("ok, pasa por aqui2");
    int index = isValueInArray(available_trades, size_av_tr, to_upper_from);
    if (index < 0) { return 0; }
    return 1 / trade_values[index];
  }
  else {
    //printf("ok, pasa por aqui3");
    int index = isValueInArray(available_trades, size_av_tr, to_upper_from);
    //printf("\nindex1: %i", index);
    if (index < 0) { return 0; }
    float semi = (1 * acc / trade_values[index]) / acc;
    index = isValueInArray(available_trades, size_av_tr, to_upper_to);
    //printf("\nindex2: %i", index);
    if (index < 0) { return 0; }
    float comp = (acc * trade_values[index] / 1) / acc;
    return semi * comp;
  }
}

int isValueInArray(char arr[], int size_av_tr, char searched_char) {
  for (int i = 0; i < size_av_tr; ++ i) {
    //printf("\n%c", arr[i]);
    //printf("\n%c", searched_char);
    if (arr[i] == searched_char) {
      return i;
    }
  }
  return -1;
}