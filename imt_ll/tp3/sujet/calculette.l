%{
extern int yylval;
#include "y.tab.h"
%}
%%
[0-9]+     { yylval = atoi(yytext); return Nombre; }
\+              { return PLUS; }
\-		{ return MOINS; }
\*              { return FOIS; }
\/		{ return DIV; }
\(              { return PAROU;}
\)              { return PARFER;}
[ \t]           {}
\n              { return RETURN; }
.               { return ERROR;}
%%
