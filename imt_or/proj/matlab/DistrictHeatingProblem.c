/***--------------- Mathematical Model of DISTRICT HEATING NETWORK OPTIMIZATION -----------------***/


/***--------------- Sets -----------------***/
set V; /* Set of all Nodes */
set V0; /* Set of Origin Nodes*/
set E within V cross V; /* Total Set of Edges*/


/***--------------- Set of Parameters -----------------***/
param cfix{i in V, j in V}; /* Fixed Investment Cost "euro/m" */
param cvar{i in V, j in V}; /* Variable Investment Cost "euro/(m kW)" */
param com{i in V, j in V}; /* Operation & Maintenance Cost "euro/(m a)" */
param cheat{i in V}; /* Heat Generation Cost "euro/(kW h)" */
param crev{i in V, j in V}; /* Revenue for Delivered Heat "euro/(kW h)" */
param Alpha; /* Annuity Factor for Investment Cost "1/a" */
param vfix{i in V, j in V}; /* Fixed Thermal Losses "kW/m" */
param vvar{i in V, j in V}; /* Variable Thermal Losses "kW/(kW m)" */
param Tflh; /* Full Load Hours of Source Vertices "h/a" */
param Betta; /* Concurrence Effect "1" */
param Lambda; /* Connect Quota "1" */

param L{i in V, j in V}; /* Edge Length "m" */
param d{i in V, j in V}; /* Edge Peak Demand "kW" */
param D{i in V, j in V}; /* Edge Peak Demand "kWh/a" */
param Cmax{i in V, j in V}; /* Maximum Pipe Capacity "kW" */
param Qmax{i in V}; /* Source Vertex Capacity "kW" */
param cumd{i in V, j in V}; /* Penalty of Unmet Demand */


/***--------------- Set of Dependent Parameters -----------------***/
param Etta{i in V, j in V}:= 1 - L[i,j]*vvar[i,j];
param Delta{i in V, j in V}:= d[i,j] * Betta * Lambda + L[i,j] * vfix[i,j];


/***--------------- Set of Variables -----------------***/
var x{i in V, j in V} binary;
var Pin{i in V, j in V} >=0;
var Pout{i in V, j in V} >=0;

/***--------------- Set of Auxilary Variables -----------------***/

var TotalRevenue;
var TotalHeatGenerationCost;
var TotalMaintenanceCost;
var TotalFixedInvestmentCost;
var TotalVariableInvestmentCost;
var UnmetDemandPenalty;
var ObjectiveValue;

/***--------------- Objective Function -----------------***/
minimize cost: ObjectiveValue;


/***--------------- Constraints -----------------***/
s.t. Const1: sum{(i,j) in E: i<>j} x[i,j] = 7;
s.t. Const2{(i,j) in E: i<>j}: x[i,j]+x[j,i] <=1;
s.t. Const3{(i,j) in E: i<>j}: Etta[i,j] * Pin[i,j] - Pout[i,j] = Delta[i,j] * x[i,j];
s.t. Const4{i in V: i <> 5}: sum{m in V: m<>i and m <>5} Pin[i,m] = sum{m in V: m<>i} Pout[m,i];
s.t. Const5{(i,j) in E: i<>j}: Pin[i,j] <= 10*Cmax[i,j]*x[i,j];
s.t. Const6{j in V0}: sum{i in V:i<>j} x[i,j] = 0;
s.t. Const7{i in V0}: sum{j in V: j<>i} Pin[i,j] <= Qmax[i];
s.t. Const8{i in V: i<>5}: sum{j in V: j <>i} x[j,i] >=1;

/***--------------- Constraints: Objective Terms -----------------***/

s.t. const9: TotalRevenue = sum{(i,j) in E} (crev[i,j] * D[i,j] * Lambda * x[i,j]);
s.t. const10: TotalHeatGenerationCost = sum{i in V0} (Tflh * cheat[i] / Betta * sum{j in V: j<>i} Pin[i,j]);
s.t. const11: TotalMaintenanceCost = sum{(i,j) in E} (com[i,j] * L[i,j] * x[i,j]);
s.t. const12: TotalFixedInvestmentCost = sum{(i,j) in E} (cfix[i,j] * L[i,j] * Alpha * x[i,j]);
s.t. const13: TotalVariableInvestmentCost = sum{(i,j) in E}(cvar[i,j] * L[i,j] * Alpha * Pin[i,j]);
s.t. const14: UnmetDemandPenalty = sum{(i,j) in E} (0.5*cumd[i,j]*D[i,j]*(1-x[i,j]-x[j,i]));
s.t. const15: ObjectiveValue = TotalHeatGenerationCost + TotalMaintenanceCost + TotalFixedInvestmentCost + TotalVariableInvestmentCost + UnmetDemandPenalty - TotalRevenue;


/***--------------- Execution Body and Final Result Showing -----------------***/
solve;

display x;
display Pin;
display Pout;
display cost;


/***--------------- Inputs and Data -----------------***/
data;

set V := 1 2 3 4 5 6 7 8;
set V0 :=  5;

set E:= (1,2) (1,3) (1,4) (1,5) (1,6) (1,7) (1,8) (2,1) (2,3) (2,4) (2,5) (2,6) (2,7) (2,8) (3,1) (3,2) (3,4) (3,5) (3,6) (3,7) (3,8) (4,1) (4,2) (4,3) (4,5) (4,6) (4,7) (4,8) (5,1) (5,2) (5,3) (5,4) (5,6) (5,7) (5,8) (6,1) (6,2) (6,3) (6,4) (6,5) (6,7) (6,8) (7,1) (7,2) (7,3) (7,4) (7,5) (7,6) (7,8) (8,1) (8,2) (8,3) (8,4) (8,5) (8,6) (8,7);

param cfix:     1       2       3       4       5       6       7       8:=
	1	0	1414	2828	1414	3162	4000	3162	2828
	2	1414	0	1414	2000	2000	3162	2828	3162
	3	2828	1414	0	3162	1414	2828	3162	4000
	4	1414	2000	3162	0	2828	3162	2000	1414
	5	3162	2000	1414	2828	0	1414	2000	3162
	6	4000	3162	2828	3162	1414	0	1414	2828
	7	3162	2828	3162	2000	2000	1414	0	1414
	8	2828	3162	4000	1414	3162	2828	1414	0;

param crev:     1    	2	3    	4    	5    	6    	7    	8:=
	1	0	32	29	30	10	15	28	17
	2	32	0	16	33	38	25	17	23
	3	29	16	0	32	40	27	24	26
	4	30	33	32	0	19	23	31	27
	5	10	38	40	19	0	33	17	32
	6	15	25	27	23	33	0	38	10
	7	28	17	24	31	17	38	0	30
	8	17	23	26	27	32	10	30	0;


param cheat:=   1 3 
		2 1 
		3 2 
		4 4 
		5 5 
		6 1 
		7 2 
		8 3;


param cvar:     1    	2	3    	4    	5    	6    	7    	8:=
	1	0	5	2	2	2	9	6	9
	2	5	0	9	7	4	9	5	7
	3	2	9	0	3	4	6	8	9
	4	2	7	3	0	3	3	4	3
	5	2	4	4	3	0	2	3	4
	6	9	9	6	3	2	0	4	7
	7	6	5	8	4	3	4	0	6
	8	9	7	9	3	4	7	6	0;


param com:      1    	2	3    	4    	5    	6    	7    	8:=
	1	0	13	19	11	15	16	17	17
	2	13	0	20	19	18	14	17	18
	3	19	20	0	17	12	16	20	11
	4	11	19	17	0	12	12	13	17
	5	15	18	12	12	0	14	13	20
	6	16	14	16	12	14	0	13	11
	7	17	17	20	13	13	13	0	16
	8	17	18	11	17	20	11	16	0;


param Alpha := 0.067;

param vfix :    1       2       3       4       5       6       7       8 :=
	1	0	20	16	19	22	16	17	19
	2	20	0	20	15	20	22	16	22
	3	16	20	0	21	19	22	15	19
	4	19	15	21	0	20	23	19	21
	5	22	20	19	20	0	18	24	24
	6	16	22	22	23	18	0	19	19
	7	17	16	15	19	24	19	0	23
	8	19	22	19	21	24	19	23	0;


param vvar :    1       2       3       4       5       6       7       8 := 
	1	0.00000	0.00019	0.00027	0.00027	0.00028	0.00022	0.00025	0.00019	
	2	0.00025	0.00000	0.00022	0.00022	0.00024	0.00023	0.00018	0.00020	
	3	0.00020	0.00024	0.00000	0.00019	0.00020	0.00026	0.00027	0.00021	
	4	0.00027	0.00019	0.00025	0.00000	0.00027	0.00025	0.00025	0.00022	
	5	0.00027	0.00018	0.00020	0.00020	0.00000	0.00025	0.00026	0.00025	
	6	0.00019	0.00022	0.00024	0.00025	0.00025	0.00000	0.00023	0.00021	
	7	0.00021	0.00024	0.00028	0.00026	0.00026	0.00027	0.00000	0.00021	
	8	0.00026	0.00021	0.00027	0.00027	0.00025	0.00024	0.00020	0.00000;


param Tflh := 1800;

param Betta := 0.7;
param Lambda := 0.7;

param L :       1       2       3       4       5       6       7       8 :=
	1	0	14	28	14	32	40	32	28
	2	14	0	14	20	20	32	28	32
	3	28	14	0	32	14	28	32	40
	4	14	20	32	0	28	32	20	14
	5	32	20	14	28	0	14	20	32
	6	40	32	28	32	14	0	14	28
	7	32	28	32	20	20	14	0	14
	8	28	32	40	14	32	28	14	0;

param d :       1       2       3       4       5       6       7       8 :=
	1	0	14	27	37	34	27	32	26
	2	14	0	18	40	10	25	36	19
	3	27	18	0	39	18	16	12	11
	4	37	40	39	0	32	37	20	15
	5	34	10	18	32	0	34	18	10
	6	27	25	16	37	34	0	20	12
	7	32	36	12	20	18	20	0	34
	8	26	19	11	15	12	12	34	0;

param D :       1       2       3       4       5       6       7       8 :=
	1	0	241	236	213	205	178	228	195
	2	241	0	221	240	168	229	199	165
	3	236	221	0	197	248	176	246	240
	4	213	240	197	0	198	190	212	158
	5	205	168	248	198	0	245	195	178
	6	178	229	176	190	245	0	224	243
	7	228	199	246	212	195	224	0	180
	8	195	165	240	158	178	243	180	0;


param Cmax :    1       2       3       4       5       6       7       8 :=
	1	0	390	504	439	387	561	626	470
	2	390	0	488	517	357	535	484	592
	3	504	488	0	632	474	639	640	613
	4	439	517	632	0	507	608	557	424
	5	387	357	474	507	0	369	372	650
	6	561	535	639	608	369	0	526	541
	7	626	484	640	557	372	526	0	627
	8	470	592	613	424	650	541	627	0;


param cumd :    1    	2	3    	4    	5    	6    	7    	8:=
	1	0	32	29	30	10	15	28	17
	2	32	0	16	33	38	25	17	23
	3	29	16	0	32	40	27	24	26
	4	30	33	32	0	19	23	31	27
	5	10	38	40	19	0	33	17	32
	6	15	25	27	23	33	0	38	10
	7	28	17	24	31	17	38	0	30
	8	17	23	26	27	32	10	30	0;


param Qmax :=   1 0 
		2 0 
		3 0 
		4 0 
		5 30000 
		6 0 
		7 0 
		8 0;

end;
