#include <stdio.h>

extern int yylineno;
extern char  yytext[];

yyerror(s) {
  /* printf( "Erreur ligne %d, symbole: %s\n", yylineno, yytext); */
  printf( "Desole, une erreur a ete detectee : %s\n" , s); exit(1);
}

main() {
 
  yyparse();
  printf("\nJ'ai fini!\n");
}
