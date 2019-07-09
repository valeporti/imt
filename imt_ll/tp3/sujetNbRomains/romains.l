%{
#include "y.tab.h"
%}
%%
i    {return I;}
v    {return V;}
x    {return X;}
l    {return L;}
c    {return C;}
\n   {return RETURN;}
.    {return ERROR; }
%%
