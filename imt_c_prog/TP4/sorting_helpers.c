#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "helpers.h"
#include "sorting_helpers.h"

void sort_as_requested(company_stock *base, int size_base, int choix_in) {
  if (choix_in == 1) {
    qsort(base, size_base, sizeof(company_stock), compareStr);
  }
  else if (choix_in == 2) {
    qsort(base, size_base, sizeof(company_stock), compareLastQty);
  }
  else if (choix_in == 3) {
    qsort(base, size_base, sizeof(company_stock), compareLastAbs);
  }
  else if (choix_in == 4) {
    qsort(base, size_base, sizeof(company_stock), compareRelCh);
  }
  else if (choix_in == 5) {
    qsort(base, size_base, sizeof(company_stock), compareVolume);
  }  
}

int compareStr(const void *el_a, const void *el_b) {
  company_stock a = *((company_stock*)el_a);
  company_stock b = *((company_stock*)el_b);
  return strcmp(a.name, b.name);
}

int compareLastQty(const void *el_a, const void *el_b) {
  company_stock a = *((company_stock*)el_a);
  company_stock b = *((company_stock*)el_b);
  return comparefloats(a.last_price, b.last_price);
}

int compareLastAbs(const void *el_a, const void *el_b) {
  company_stock a = *((company_stock*)el_a);
  company_stock b = *((company_stock*)el_b);
  return comparefloats(a.abs_last_price, b.abs_last_price);
}

int compareRelCh(const void *el_a, const void *el_b) {
  company_stock a = *((company_stock*)el_a);
  company_stock b = *((company_stock*)el_b);
  return comparefloats(a.rel_price_change, b.rel_price_change);
}

int compareVolume(const void *el_a, const void *el_b) {
  company_stock a = *((company_stock*)el_a);
  company_stock b = *((company_stock*)el_b);
  return comparefloats(a.volume, b.volume);
}

int comparefloats(float a, float b) {
  if (a < b) { return -1; }
  else if (a > b) { return 1; }
  else {return 0;}
}