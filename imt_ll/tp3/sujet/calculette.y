%token ERROR RETURN
%token Nombre FOIS DIV PLUS MOINS PAROU PARFER
%%

sequence : instruction RETURN sequence
         | RETURN   { printf("Retun Seq\n"); exit(0); }
         | ERROR    { printf("Undefined Symbol\n"); exit(1);}

instruction : expr    { printf("--> %d\n", $1); }

expr: expr PLUS terme   { $$ = $1 + $3; }
    | expr MOINS terme	{ $$ = $1 - $3; }
    | terme

terme: terme FOIS facteur 	{ $$ = $1 * $3; }
    | terme DIV facteur	{ if ($3 == 0) { printf("Div BY 0!!\n"); exit(2); } else  $$ = $1 / $3; }
    | facteur

facteur: PAROU expr PARFER  { $$ = $2; }
    | Nombre
%%
