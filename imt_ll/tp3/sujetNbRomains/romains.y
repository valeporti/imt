%token ERROR RETURN
%token V I X L C
%%
 romains : romain
	| romain romains

 romain : dizaines  RETURN { printf("Valeur : %d\n", $1); }

 dizaines : croix unites	{ }
	| X L unites	{  }
	| L croix unites{  }
	| X C unites	{ }

 croix :		{ }
 	| X		{ }
	| X X		{ }
	| X X X		{ }

 unites : I V 		{}
        | I X 		{}
        | V batons	{ }
        | batons

  batons : 		{ $$ = 0; }
        | I		{ $$ = 1; }
        | I I		{ $$ = 2; }
        | I I I		{ $$ = 3; }
%%
