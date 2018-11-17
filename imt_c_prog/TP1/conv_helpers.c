#include<stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include<assert.h> /* BUT https://www.softwariness.com/articles/assertions-in-cpp/ */

#ifdef	NDEBUG
#define assert_condition(x, true_msg);
#else
#define assert_condition(x, true_msg) (x) ? printf("Success %s.%i: \u2714 - %s\n", __FILE__, __LINE__, true_msg) : assert(x);
#endif

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
    int index = isValueInArray(available_trades, size_av_tr, to_upper_to);
    assert_condition(index, "to_upper_from == to_upper_pivot");
    if (index < 0) { return 0; }
    return trade_values[index];
  }
  else if (to_upper_to == to_upper_pivot) {
    int index = isValueInArray(available_trades, size_av_tr, to_upper_from);
    assert_condition(1,"to_upper_to == to_upper_pivot");
    if (index < 0) { return 0; }
    return 1 / trade_values[index];
  }
  else {
    int index = isValueInArray(available_trades, size_av_tr, to_upper_from);
    assert_condition(1, " else");
    if (index < 0) { return 0; }
    float semi = (1 * acc / trade_values[index]) / acc;
    index = isValueInArray(available_trades, size_av_tr, to_upper_to);
    assert_condition(1, " else2");
    if (index < 0) { return 0; }
    float comp = (acc * trade_values[index] / 1) / acc;
    return semi * comp;
  }
}

int isValueInArray(char arr[], int size_av_tr, char searched_char) {
  assert_condition(1, "starting search char");
  for (int i = 0; i < size_av_tr; ++ i) {
    if (arr[i] == searched_char) {
      assert_condition(1, "Char found");
      return i;
    }
  }
  assert_condition(1, "No char found");
  return -1;
}