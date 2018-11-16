set I; # canning  plants
set J; # markets
param a{i in I};
/*  capacity  of  plant i in cases  */
param b{j in J};
/*  demand  at  market j in cases  */
param d{i in I, j in J};
/*  distance  in  thousands  of miles  */
param f;
/*  freight  in USD  per  case  per  thousand  miles  */
param c{i in I, j in J} := f * d[i,j];
/*  transport  cost in  thousands  of USD  per  case */

var x{i in I, j in J} >= 0;
/*  shipment  quantities  in cases  */

minimize  cost: sum{i in I, j in J} c[i,j]*x[i,j];
/*  total  transportation  costs  in  thousands  of  dollars  */

s.t. supply{i in I}: sum{j in J} x[i,j] <= a[i];
/*  observe  supply  limit  at plant i */
s.t. demand{j in J}: sum{i in I} x[i,j] >= b[j];
/*  satisfy  demand  at  market j */

solve;
display x;
display  cost;

data;
set I :=  Seattle San-Diego;
set J := New-York  Chicago  Kansas;
param a :=  	Seattle    350
		San-Diego  650;
param b := 	New-York   300
		Chicago    300
		Kansas     300;
param d :   	New-York  Chicago  Kansas  :=
	Seattle     2.5        1.7      1.8
	San-Diego   2.5        1.8      1.4;
param f := 90;

end;
