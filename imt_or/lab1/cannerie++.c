
/*  GENERAL PARAMETERS */
set I; # canning  plants
set J; # markets
param a{i in I};
/*  capacity  of  plant i in cases  */
param fc{i in I};
/*  capacity fixed cost i in cases */
param b{j in J};
/*  demand  at  market j in cases  */
param d{i in I, j in J};
/*  distance  in  thousands  of miles  */
param f;
/*  freight  in USD  per  case  per  thousand  miles  */
param c{i in I, j in J} := f * d[i,j];
/*  transport  cost in  thousands  of USD  per  case */


/*  DECISION VARIABLES */
var x{i in I, j in J} >= 0;
/*  shipment  quantities  in cases  */
var y{i in I} binary;
/*  plant i participates as supplier or not  */


/*  OBJECTIVE FUNCTION */
minimize  cost: sum{i in I, j in J} (c[i,j]*x[i,j]+fc[i]*y[i]);
/*  total  transportation  costs  in  thousands  of  dollars  */

/*  CONSTRAINTS */
s.t. supply{i in I}: sum{j in J} x[i,j] <= a[i] * y[i];
/*  observe  supply  limit  at plant i */
s.t. demand{j in J}: sum{i in I} x[i,j] >= b[j];
/*  satisfy  demand  at  market j */
s.t. number_of_plants: sum{i in I} y[i] <= 3;
/*  need maximum 3 plants */


solve;
display x;
display y;
display cost;
display sum{i in I, j in J} x[i,j];
display sum{i in I} b[i];


data;
set I := 1 2 3 4 5 6 7 8;
set J := 1 2 3 4 5 6 7 8 9 10;
param a :=  	1    	200
		2	300
		3	150
		4	180
		5	280
		6	270
		7	200
		8	220;
param fc := 	1    	684
		2	977
		3	563
		4	612
		5	950
		6	928
		7	750
		8	766;	
param b := 	1	80
		2	50
		3	82
		4	43
		5	96
		6	107
		7	88
		8	42	
		9	65	
		10	38;
param d :   	1 2 3 4 5 6 7 8 9 10  :=
	1	18	14	12	16	19	17	14	18	11	13
	2	12	15	17	19	13	10	15	14	16	14
	3	11	12	12	20	19	20	12	15	13	16
	4	11	18	10	10	11	15	13	15	10	15
	5	10	14	20	10	10	16	18	16	15	15
	6	12	14	20	14	15	10	12	15	17	13
	7	13	17	19	15	12	12	12	14	20	14
	8	11	10	12	18	18	17	19	20	15	10;
param f := 90;


end;
