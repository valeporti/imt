/* ?? should we cosider that there are existing already pipes ?? ?*/
/* ?? how to treat the PijIn and Out, how to calculate them since they are dependant ?? ?*/
/* we don't have Q_max */
/* Issues with expected units */


/* Main */
set I; /* Source Vertex */
set J;  /* Destination Vertex */

/* PARAMETERS */

/* edges */
param node_coord_x{i in I};
param node_coord_y{i in I};

param c_fix{i in I, j in J};/* Fixed investment cost at edge e ij (e /m) */
param c_var{i in I, j in J};/* Variable investment cost at edge e ij (e /(m kW)) */
param c_om{i in I, j in J};/* Operation & Maintenance cost at edge e ij (e /(m a)) */
param c_rev{i in I, j in J};/* Revenue for delivered heat at edge e ij (e /kWh) */
param p_umd{i in I, j in J};/*Penalty of unmet demand at edge e ij (e /kW)*/
param tl_fix{i in I, j in J};/*Fixed thermal loss at edge e ij (kW/m)*/
param tl_var{i in I, j in J};/*Variable thermal loss at edge e ij (kW/(kW m))*/
/*param l{i in I, j in J};*//* Length of edge e ij (m) */
param d{i in I, j in J};/* Potential peak demand at edge e ij (kW) */
param D{i in I, j in J};/* Potential annual peak demand at edge e ij (kW) */
param C_max{i in I, j in J};/* Maximum pipe capacity at edge e ij (kW) */
param Q_max;/*{i in I, j in J};/* Source vertex capacity of heat generation (kW) */
/* vertex*/
param c_heat{i in I};/* Heat generation cost of source i = v 0 (e /kWh) */
param T_flh; /*{i in I};/*Full load hours of the source i = v 0 (h/kW)*/

/* factors */
param beta;/* Concurrence effect */
param lamda;/* Connect quota */
param alpha;/* Annuity factor for investment costs (1/a) */
param source;
param fixed_unit_cost;
param total_vertices:= (sum{i in I} 1);

/* DEFINITIONS */
/* dependances */
/*
s.t. REVENUE{i in I, j in J}: lamda * x[i, j] * c_rev[i, j] * D[i, j]; 
s.t. UNMET_DEM_PENALITY{i in I, j in J} : (1 - x[i, j]) * (d[i, j] - (tl_fix[i, j] * l[i, j] + tl_var[i, j] * l[i, j]));
s.t. FIXED_INV_COST{i in I, j in J} : alpha * x[i, j] * c_fix[i, j] * l[i, j];
s.t. MAINT_COST{i in I, j in J} : c_om[i, j] * l[i, j] * x[i, j];
param HEAT_GEN_COST{i in I} := (1 / beta) * T_flh[source] * c_heat[source]; 
param VAR_INV_COST{i in I, j in J} := alpha * c_var[i, j] * l[i, j];
*/


/* variables */
var x{i in I, j in J} binary;
var P_in{i in I, j in J} >= 0;
var P_out{i in I, j in J} >= 0;


/* sub expressions */
param l{i in I, j in J: i<>j} := sqrt((node_coord_x[i] - node_coord_x[j]) * (node_coord_x[i] - node_coord_x[j]) + (node_coord_y[i] - node_coord_y[j]) * (node_coord_y[i] - node_coord_y[j]));
param eta{i in I, j in J: i<>j} := 1 - l[i, j] * tl_var[i, j];
/*display eta;*/
param delta{i in I, j in J: i<>j} := beta * lamda * d[i, j] + l[i, j] * tl_fix[i, j];

/* Objective Function */
minimize Z: 
	(sum{i in I, j in J: i<>j} (c_rev[i, j] * D[i, j] * x[i, j] * lamda)) +
	(T_flh * c_heat[source] / beta) * (sum{j in J} (P_in[source, j])) +
	(sum{i in I, j in J: i<>j} c_om[i, j] * l[i, j] * x[i, j]) + 
	(sum{i in I, j in J: i<>j} c_fix[i, j] * l[i, j] * alpha * x[i, j]) + 
	(sum{i in I, j in J: i<>j} c_var[i, j] * l[i, j] * alpha * P_in[i, j]) + 
	0.5 * (sum{i in I, j in J: i<>j} (p_umd[i, j] * D[i, j])*(1 - x[i, j] - x[j, i]));
	

/* CONSTRAINTS */
s.t. tree_structure: total_vertices - 1 = sum{i in I, j in J: i<>j} x[i, j];

s.t. unidirectionality{i in I, j in J: i<>j}: x[i, j] + x[j, i] <= 1; 

s.t. demand_satisfaction{i in I, j in J: i<>j}: eta[i, j] * P_in[i, j] - P_out[i, j] = x[i, j] * delta[i, j]; /* "Always make the variables met in an equation" */

s.t. flow_equilibrium_at_each_vertex{j in J: j <> source}: sum{i in I} P_in[i, j] = sum{i in I} P_out[j, i];/* Pin i->j == P j->k */  /* HOW TO */

s.t. edge_capacity{i in I, j in J: i<>j}: P_in[i, j] <= C_max[i, j] * x[i, j];

s.t. source_structural: sum{i in I: i <> source} x[i, source] = 0;

s.t. source_heat_generation: sum{j in J: j <> source} P_in[source, j] <= Q_max; /* Pin ij <= Q max (it should be just invertices, even an unique parameter*/ 

s.t. tour_elimination{i in I}: sum{j in J: j <> i} x[j, i] >= 1;


/* solving instructions */
solve;
display l;

/* DATA */
data;
set I := 1 2 3 4 5 6 7 8;
set J := 1 2 3 4 5 6 7 8;
param source := 4;
param T_flh := 1800;
param alpha := 0.067;
param beta := 0.7;
param lamda := 0.7 ; /* before, gamma */
param Q_max := 3000;
param fixed_unit_cost := 100;
param node_coord_x :=
	1	10
	2	20
	3	30
	4	20
	5	40
	6	50
	7	40
	8	30;
param node_coord_y :=
	1	30
	2	40
	3	50
	4	20
	5	40
	6	30
	7	20
	8	10;
param tl_fix : 1 2 3 4 5 6 7 8 :=	
1	0.00000	0.00019	0.00027	0.00027	0.00028	0.00022	0.00025	0.00019
2	0.00025	0.00000	0.00022	0.00022	0.00024	0.00023	0.00018	0.00020
3	0.00020	0.00024	0.00000	0.00019	0.00020	0.00026	0.00027	0.00021
4	0.00027	0.00019	0.00025	0.00000	0.00027	0.00025	0.00025	0.00022
5	0.00027	0.00018	0.00020	0.00020	0.00000	0.00025	0.00026	0.00025
6	0.00019	0.00022	0.00024	0.00025	0.00025	0.00000	0.00023	0.00021
7	0.00021	0.00024	0.00028	0.00026	0.00026	0.00027	0.00000	0.00021
8	0.00026	0.00021	0.00027	0.00027	0.00025	0.00024	0.00020	0.00000;
param tl_var : 1 2 3 4 5 6 7 8 :=
1	0	20	16	19	22	16	17	19
2	20	0	20	15	20	22	16	22
3	16	20	0	21	19	22	15	19
4	19	15	21	0	20	23	19	21
5	22	20	19	20	0	18	24	24
6	16	22	22	23	18	0	19	19
7	17	16	15	19	24	19	0	23
8	19	22	19	21	24	19	23	0;

param c_var : 1 2 3 4 5 6 7 8 :=
1	0	5	2	2	2	9	6	9
2	5	0	9	7	4	9	5	7
3	2	9	0	3	4	6	8	9
4	2	7	3	0	3	3	4	3
5	2	4	4	3	0	2	3	4
6	9	9	6	3	2	0	4	7
7	6	5	8	4	3	4	0	6
8	9	7	9	3	4	7	6	0;
param c_fix : 1 2 3 4 5 6 7 8 :=
1	0	1414	2828	1414	3162	4000	3162	2828
2	1414	0	1414	2000	2000	3162	2828	3162
3	2828	1414	0	3162	1414	2828	3162	4000
4	1414	2000	3162	0	2828	3162	2000	1414
5	3162	2000	1414	2828	0	1414	2000	3162
6	4000	3162	2828	3162	1414	0	1414	2828
7	3162	2828	3162	2000	2000	1414	0	1414
8	2828	3162	4000	1414	3162	2828	1414	0;
param c_heat :=
1	3
2	1
3	2
4	4
5	5
6	1
7	2
8	3;
param c_om : 1 2 3 4 5 6 7 8 :=
1	0	13	19	11	15	16	17	17
2	13	0	20	19	18	14	17	18
3	19	20	0	17	12	16	20	11
4	11	19	17	0	12	12	13	17
5	15	18	12	12	0	14	13	20
6	16	14	16	12	14	0	13	11
7	17	17	20	13	13	13	0	16
8	17	18	11	17	20	11	16	0;
param c_rev : 1 2 3 4 5 6 7 8 :=
1	0	32	29	30	10	15	28	17
2	32	0	16	33	38	25	17	23
3	29	16	0	32	40	27	24	26
4	30	33	32	0	19	23	31	27
5	10	38	40	19	0	33	17	32
6	15	25	27	23	33	0	38	10
7	28	17	24	31	17	38	0	30
8	17	23	26	27	32	10	30	0;

param d : 1 2 3 4 5 6 7 8 :=
	1	0	14	27	37	34	27	32	26
	2	14	0	18	40	10	25	36	19
	3	27	18	0	39	18	16	12	11
	4	37	40	39	0	32	37	20	15
	5	34	10	18	32	0	34	18	10
	6	27	25	16	37	34	0	20	12
	7	32	36	12	20	18	20	0	34
	8	26	19	11	15	12	12	34	0;

param D : 1 2 3 4 5 6 7 8 :=
	1	0	241	236	213	205	178	228	195
	2	241	0	221	240	168	229	199	165
	3	236	221	0	197	248	176	246	240
	4	213	240	197	0	198	190	212	158
	5	205	168	248	198	0	245	195	178
	6	178	229	176	190	245	0	224	243
	7	228	199	246	212	195	224	0	180
	8	195	165	240	158	178	243	180	0;

param C_max : 1 2 3 4 5 6 7 8 :=
	1	0	390	504	439	387	561	626	470
	2	390	0	488	517	357	535	484	592
	3	504	488	0	632	474	639	640	613
	4	439	517	632	0	507	608	557	424
	5	387	357	474	507	0	369	372	650
	6	561	535	639	608	369	0	526	541
	7	626	484	640	557	372	526	0	627
	8	470	592	613	424	650	541	627	0;

param p_umd : 1 2 3 4 5 6 7 8 :=	
	1 	0	32	29	30	10	15	28	17
	2 	32	0	16	33	38	25	17	23
	3 	29	16	0	32	40	27	24	26
	4 	30	33	32	0	19	23	31	27
	5 	10	38	40	19	0	33	17	32
	6 	15	25	27	23	33	0	38	10
	7 	28	17	24	31	17	38	0	30
	8 	17	23	26	27	32	10	30	0;






