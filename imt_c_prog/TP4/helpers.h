
#define MAX_FNAME_LENGTH 256

struct company_stock_structure
{
  char name[MAX_FNAME_LENGTH];
  float last_price;
  float abs_last_price;
  float rel_price_change;
  float volume;
};
typedef struct company_stock_structure company_stock;

void removeSpaces(char *str) ;
void initializeStr(char *str, int n);
void getStr(char *from_str, char *to_str, int from, int n);

/*

all: 2.1.o helpers.o sorting_helpers.o
	gcc 2.1.o helpers.o sorting_helpers.o -o 2.1.out

2.1.o: 2.1.c 
	gcc -c 2.1.c

helpers.o: helpers.c
	gcc helpers.c

sorting_helpers.o: sorting_helpers.c
	gcc sorting_helpers.c

clean:
	rm 2.1.o helpers.o sorting_helpers.o
  */