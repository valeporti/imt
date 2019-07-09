#include <stdio.h>

extern int yylineno;
extern char  yytext[];

yyerror() {
  /* printf( "Erreur ligne %d, symbole: %s\n", yylineno, yytext);*/
  printf( "Desole, salut, bonne chance\n"); exit(1);
}

main() {
  yyparse();
  printf("\nJ'ai fini!\n");
}
