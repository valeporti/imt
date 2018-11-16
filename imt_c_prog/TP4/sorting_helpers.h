/* declare functions */
int compareStr(const void *el_a, const void *el_b);
int comparefloats(float a, float b);
int compareLastQty(const void *el_a, const void *el_b);
int compareLastAbs(const void *el_a, const void *el_b);
int compareRelCh(const void *el_a, const void *el_b);
int compareVolume(const void *el_a, const void *el_b);
void sort_as_requested(company_stock *base, int size_base, int choix_in);
