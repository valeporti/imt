/* libraries */
#include<stdio.h>
#include <ctype.h>
#include "conv_helpers.h"
#include<assert.h> /* BUT https://www.softwariness.com/articles/assertions-in-cpp/ */

#ifdef	NDEBUG
#define assert_condition(x, true_msg);
#else
#define assert_condition(x, true_msg) (x) ? printf("Success %s.%i: \u2714 - %s\n", __FILE__, __LINE__, true_msg) : assert(x);
#endif

void main() {

  // variables decalration
  float USD = 1;
  float EURO = 0.87;
  float POUND = 0.77;
  char own_balance;

  // presentation
  printf("\nThe trading balances that this program knows/uses are:\n*taking as pivot the USD dollar\n");
  printf("----------------------------\n");
  printf("USD = %f %s\n", USD, get_value_form_char('U'));
  printf("1 %s = %f %s\n", get_value_form_char('U'), EURO, get_value_form_char('E'));
  printf("1 %s = %f %s\n", get_value_form_char('U'), POUND, get_value_form_char('P'));
  printf("----------------------------\n");

  // get in contact with user
  printf("\nWould you like to use your own balances?\nInstructions\n--> for YES write 'Y', for NO 'N'\n");
  scanf(" %c", &own_balance);

  assert_condition(1, "printed instructions");

  // handle input and retrieve values if necessary
  switch(toupper(own_balance))
  {
    case 'Y':
    {
      printf("\n");
      printf("Please, write the values using as reference the USD dollar:\n");
      printf("for EURO:\n1 USD =  ");
      scanf(" %f", &EURO);
      printf("for POUND:\n1 USD =  ");
      scanf(" %f", &POUND);
      break;
    }
    case 'N':
    {
      break;
    }
    default: 
    {
      printf("Sorry, we didn't recognize the input :S");
    }
  }
  printf("\n");

  assert_condition(1, "Got correct input or transformed it");

  char from;
  char to;
  float from_calc;
  float to_calc;
  float number;

  printf("----------- Let's START!! :) -----------\n");
  printf("Please, indicate the trading balance you want to perform.\n");
  printf("FROM (write one: 'E' or 'U' or 'P', to indicate Euro or USD dollar or Pound)\n");
  scanf(" %c", &from);
  printf("TO (write one: 'E' or 'U' or 'P', to indicate Euro or USD dollar or Pound)\n");
  scanf(" %c", &to);
  printf("Quantity to transform (number):\n");
  scanf(" %f", &number);

  assert_condition(1, "Grabbed values to do calculations");

  // calculations
  int size_av_tr = 2;
  char available_trades[] = {'P', 'E'};
  char pivot = 'U';
  float trade_values[] = {POUND, EURO};
  float result = get_corresponding_ratio(available_trades, size_av_tr, trade_values, from, to, pivot) * number;
  char* from_sign = get_value_form_char(from);
  char* to_sign = get_value_form_char(to);
  printf("\n-----> Result... : %f %s = %f %s\n", number, from_sign, result, to_sign);
  assert_condition(1, "Success on calculations");
  
}