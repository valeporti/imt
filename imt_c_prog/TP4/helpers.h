
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