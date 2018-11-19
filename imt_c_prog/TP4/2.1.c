#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "helpers.h"
#include "sorting_helpers.h"
#include<assert.h>

#ifdef	NDEBUG
#define assert_condition(x, true_msg);
#else
#define assert_condition(x, true_msg) (x) ? printf("Success %s.%i: \u2714 - %s\n", __FILE__, __LINE__, true_msg) : assert(x);
#endif

void main(int argc, char **argv) {

  assert_condition(1, "START");

  FILE *stock;
  int total_bytes, counter = 0, char_to_extract, choix;
  company_stock *companies_info;
  char *pointer_html, *html, to_match[26] = "/finance/stocks/overview/", *sub_token, sub_coincidence[] = "\">", val[256], *token, new[256];

  if (argc == 2) {
		choix = atoi(argv[1]);
    if (choix == 0 || choix > 5) { return; }
	} else {
		printf("Program usage is as follows: ./2.1.out field\nWhere \"field\" can take values from {1,2,...5} and corresponds to the field by which the stocks will be ordered, i.e. by name, last_price, relative_change, absolute_change and volume, respectively.\n");
    return;
	}

  assert_condition(1, "Taken output from promt");

  /* Download stock info */
  system("wget --quiet --output-document stocks.txt https://www.reuters.com/finance/markets/index/.FCHI");

  assert_condition(1, "Created file 'stocks.txt' with info");

  stock = fopen("stocks.txt", "r");

  if (stock == NULL) { printf("issue op"); return; }
  assert_condition(1, "Opened 'stocks.txt' file");
  
  /* get info from file and locate pointer to the begining in order to work with it */
  fseek(stock, 0, SEEK_END);
  assert_condition(ftell(stock), "Read bytes / Non empty file");
  total_bytes = ftell(stock);
  fseek(stock, 0, SEEK_SET);
  assert_condition(!ftell(stock), "Reinitialized pointer on file");

  /* grab the text */
  html = (char*)malloc(sizeof(char) * total_bytes);
  fread(html, sizeof(char), total_bytes, stock);

  fclose(stock);
  assert_condition(1, "Read file and saved hmlt contents in array");

  /* process all coincidences */
  pointer_html = strstr(html, to_match);
  companies_info = (company_stock*)malloc(sizeof(company_stock));
  
  while( pointer_html != NULL ) {
 
    companies_info = (company_stock*)realloc(companies_info, sizeof(company_stock) * (1 + counter));
    company_stock company;
    initializeStr(company.name, 256);

    /* retrieve name */
    pointer_html = strstr(pointer_html, "\"link\">");
    pointer_html = strstr(pointer_html, ">");
    sub_token = pointer_html;
    sub_token = strstr(sub_token, "<");
    char_to_extract = sub_token - pointer_html;
    getStr(pointer_html, company.name, 1, char_to_extract - 1);
    //strncpy(company.name, pointer_html + 1, char_to_extract - 1);

    /* retrieve all other values*/
    for (int i = 0; i < 4; i ++) {
      
      initializeStr(val, 256);

      pointer_html = strstr(pointer_html, "data");
      pointer_html = strstr(pointer_html, ">");
      sub_token = pointer_html;
      sub_token = strstr(sub_token, "<");
      char_to_extract = sub_token - pointer_html;
      strncpy(val, pointer_html + 1, char_to_extract - 1);

      /* handle quantities with a comma */
      token = strtok(val, ",");
      if (token != NULL) { strcpy(new, token); token = strtok(NULL, ","); }
      while(token != NULL) {
        strcat(new, token);
        token = strtok(NULL, ",");
        strcpy(val, new);
      }

      if (i == 0) {
        company.last_price = atof(val);
      } 
      else if (i == 1) {
        company.abs_last_price = atof(val);
      }
      else if (i == 2) {
        company.rel_price_change = atof(val);
      }
      else if (i == 3) {
        company.volume = atof(val);
      }
      //printf("%s - %f\n", val, atof(val));
    }

    companies_info[counter] = company;

    counter ++; 
    pointer_html = strstr(pointer_html, to_match); /* next match */

  }

  assert_condition(1, "Gathered companies and info");

  sort_as_requested(companies_info, counter, choix);

  assert_condition(1, "Sorted as Requested");

  printf("\n");
  for (int i = 0; i < 30; i ++) {
    printf("#%i\n", i + 1);
    printf("Stock Name: %s\n", companies_info[i].name);
    printf("Stock Last Price: %f\n", companies_info[i].last_price);
    printf("Stock Relative Change: %f\n", companies_info[i].abs_last_price);
    printf("Stock Absolute Change: %f\n", companies_info[i].rel_price_change);
    printf("Stock Volume: %f\n", companies_info[i].volume);
    printf("\n");
  }

  assert_condition(1, "END");
}

