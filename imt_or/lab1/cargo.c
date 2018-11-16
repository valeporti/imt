
/*  GENERAL PARAMETERS */
set I; # cargo number
set J; # compartment

param w {i in I}; /* weight of each cargo */
param wc {j in J}; /* weight capacity of each compartment */
param v {i in I}; /* volume of each cargo */
param sc {j in J}; /* space capacity in each compartment */
param p {i in I}; /* profit for each cargo */
param sum_wc := sum{j in J} wc[j];


var c{i in I, j in J} >= 0; /* let cargo "c" of type i to be loaded in j compartment */

var sum_c;
var sum_sub_c{j in J};



/* Objective */ 
maximize profit: sum{i in I, j in J} c[i, j] * w[i] * p[i];

/* Constraints */
s.t. weight_capacity{j in J}: sum{i in I} c[i, j] * w[i] <= wc[j];
s.t. space_capacity{j in J}: sum{i in I} c[i, j] * v[i] * w[i] <= sc[j];

/*
s.t. get_sum_sub_c_val{j in J}: sum_sub_c[j] = sum{i in I} c[i, j];
s.t. get_sum_c_value: sum_c = sum{i in I, j in J} c[i, j];
s.t. proportionality_respected{j in J}: (sum_c * wc[j]) = ((sum_sub_c[j]) * sum_wc);
s.t. proportionality_front: sum{i in i} c[0] =
*/

s.t. get_sum_c_value: sum_c = sum{i in I, j in J} c[i, j];
s.t. get_sum_sub_c_val{j in J}: sum_sub_c[j] = sum{i in I} c[i, j];
s.t. proportionality_respected{j in J}: (sum_c * wc[j]) = ((sum_sub_c[j]) * sum_wc);

/*
s.t. proportionality_front: (sum_c * wc[Front]) = sum_sub_c[Front] * sum_wc;
s.t. proportionality_centre: (sum_c * wc[1]) = sum_sub_c[1] * sum_wc;
s.t. proportionality_back: (sum_c * wc[2]) = sum_sub_c[2] * sum_wc;
*/

/* Solving instructions */
solve;
display c;
display profit;
display sum_wc;
display sum_c;
display sum{i in I, j in J} c[i,j];
display sum{i in I} w[i];
display sum{i in I, j in J} c[i,j]*w[i];
display sum{j in J} (sum_c * wc[j]);
display sum{j in J} ((sum_sub_c[j]) * sum_wc);

/* Data */
data; 
set I := C1 C2 C3 C4;
set J := Front Centre Rear;
param w := 	C1 	18
			C2	15
			C3 	23
			C4 	12;
param v := 	C1 	480
			C2	650
			C3 	580
			C4 	390;
param wc := Front	10
			Centre	15
			Rear	23;
param sc := Front	6800
			Centre	8700
			Rear	5300;
param p := 	C1 	310
			C2	380
			C3 	350
			C4 	285;

end;
