
READ ME In CASE OF EMERGENCY


1. Uniform random draw

	int i;
	srand(seed);
	
	for ( i = 0; i < nbTir; ++i) {
		donnees[i] = ((double) rand())/RAND_MAX;
	}



2. Inverse transform sampling

	int i, j, pos;
	double v, diff, prec;

	for ( i = 0; i < nbTir; ++i) {
		v = d_Unif[i];

		j = 0;
		diff = fabs( v - v_F[j] );

		do {
			prec = diff;
			diff = fabs( v - v_F[++j] );
		} while( (j < nbVal) && (prec > diff) );

		pos = j - 1;

		donnees[i] = support[pos];
	}


3. Descriptive algorithm to calculate pi using a Monte Carlo approach

	Generate one by one the indicated pairs of random values from uniform distributions 
	that correspond to the x and y coordinates of the points.

	If the resulting point is inside the pre-defined circular section draw it with 
	a square (tracePoint(x, y, 's') and update accordingly the pi value estimation.

	If the resulting point is outside the pre-defined circular section draw it with 
	a circle (tracePoint(x, y, 'o') and update accordingly the pi value estimation.

	Return the estimated value of pi after all the generated pairs of random points
        have been tested (to verify if the point is inside or outside the pre-defined 
        circular section).



    Definition and initialization of variables used in the function

    double      pi = 0.;
    double      x, y;
    int         in;  /* in = points inside the circular area */
    int         all; /* all = total number of drawn points */
    int         i;

    srand( seed );                                                                                       

    in = all = 0;                                         

