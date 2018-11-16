/* ?? should ze cosider that there are existing already pipes ?? ?*/
/* ?? how to treat the PijIn and Out, how to detect wheter ?? ?*/


/* Main */
set I; /* Source Vertex */
set J;  /* Destination Vertex */

/* PARAMETERS */

/* edges */
param c_fix{i in I, j in J};/* Fixed investment cost at edge e ij (e /m) */
param c_var{i in I, j in J};/* Variable investment cost at edge e ij (e /(m kW)) */
param c_om{i in I, j in J};/* Operation & Maintenance cost at edge e ij (e /(m a)) */
param c_rev{i in I, j in J};/* Revenue for delivered heat at edge e ij (e /kWh) */
param p_umd{i in I, j in J};/*Penalty of unmet demand at edge e ij (e /kW)*/
param tl_fix{i in I, j in J};/*Fixed thermal loss at edge e ij (kW/m)*/
param tl_var{i in I, j in J};/*Variable thermal loss at edge e ij (kW/(kW m))*/
param l{i in I, j in J};/* Length of edge e ij (m) */
param d{i in I, j in J};/* Potential peak demand at edge e ij (kW) */
param D{i in I, j in J};/* Potential annual peak demand at edge e ij (kW) */
param C_max{i in I, j in J};/* Maximum pipe capacity at edge e ij (kW) */
param Q_max{i in I, j in J};/* Source vertex capacity of heat generation (kW) */
/* vertex*/
/* just 1?*/param c_heat{i in I};/* Heat generation cost of source i = v 0 (e /kWh) */
/* just 1?*/param T_flh{i in I};/*Full load hours of the source i = v 0 (h/kW)*/
/* factors */
param lamda;/* Concurrence effect */
param beta;/* Connect quota */
param alpha;/* Annuity factor for investment costs (1/a) */
param source;

/* DEFINITIONS */
param REVENUE{i in I, j in J} := lamda * c_rev[i, j] * D[i, j]; /* EUROS / a */

/* ?T_flh[0]? */ param HEAT_GEN_COST{i in I} := (1 / beta) * T_flh[source] * c_heat[i];

param MAINT_COST{i in I, j in J} := c_om[i, j] * l[i, j];

param FIXED_INV_COST{i in I, j in J} := alpha * x[i, j] * c_fix * l[i, j]; 

param VAR_INV_COST{i in I, j in J} := alpha * x[i, j] * c_var * l[i, j];;

param UNMET_DEM_PENALITY{i in I, j in J} := (1 - x[i, j]) * P;


/* variables */
var x{i in I, j in J} binary;

/* CONDITIONALS */

