#include <stdlib.h>
#include <math.h>

#include "CImg.h"

using namespace cimg_library;


/* --- Definition des constantes --- */

#define VRAI               1                             /* Gestion des "booleens" */
#define FAUX               0
#define EPSILON            1E-3                          /* Pour les tests sur reels */
#define B_ON               "%c[1m"                       /* Sorties console en gras  */
#define B_OFF              "%c[0m"

#define MAX_TIRAGES        (int) 1E6                     /* Taille max fixe tableaux de donnees */


/* --- Declaration variables globales --- */

char        ESC = 27;                                    /* Sorties console en gras */

int         vbDef = FAUX, verbose = vbDef;               /* Parametres generaux et valeurs */
int         nbiDef = 1000, nbIter = nbiDef;              /* par defaut                     */
int         sDef = 0, germe = sDef;

                                                         /* Valeurs par defaut des parametres  */
int         nbClassesDef = 50;                           /* specifiques                        */
int         dpDef = FAUX, disPoints = dpDef;             
CImgDisplay             affCarre;                        /* Deux variables d'affichage */
CImg<unsigned char>     imCarre;

/* --- Prototype des fonctions fournies --- */

void aide( char * nomComm );
void exo1( int nbTir, unsigned int seed, int nbClasses );
void exo2( int nbTir, unsigned int seed, int nbClasses );
void exo3( int nbTir, unsigned int seed );

void histogramme( double donnees[], int nbTir, double minSupport, double maxSupport, int nbClasses, double bornes[], int hist[] );
void fRepart( double v_fx[], int nbVal, double delta, double v_Fx[] );
void tracePoint( double x, double y, unsigned char forme );


/* --- Prototype des fonctions a completer --- */

void tirageUniforme( unsigned int seed, int nbTir, double donnees[] );
void tirageAlea( double d_Unif[], int nbTir, double support[], double v_F[], int nbVal, double donnees[] );
double piMC( unsigned int seed, int nbTir, double valeurs[] );

/* === Programme principal ====================================================================== */

int main( int argc, char * argv[] )
{

   int         numExo = 0;

   int         nbClasses = nbClassesDef;

   char        message[ 128 ];
   int         besoinAide = FAUX;
   int         i, j;


   putchar( '\n' );
   system( "clear" );


   /* --- Parseur des options du programme --- */

   printf( "Ligne de commande recue :\n\t" );
   for ( i = 0; i < argc; ++i ) printf( "%s ", argv[i] );
   puts( "\nAnalyse des options :" );

   if ( argc == 1 ) {
      puts( "\tAucun argument sur la ligne de commande" );
      puts( "Usage :" );
      besoinAide = VRAI;
   }

   for ( i = 1; (i < argc) && (! besoinAide ); ++i )
   {

      j = i;
      besoinAide = VRAI;
      strcpy( message, "Parametre non reconnu, mal place ou associe au mauvais exercice\nUsage :" );

      if ( !strcmp(argv[i], "-h") || !strcmp(argv[i], "-help") ) {
         sprintf( message, "Demande d'aide" );
         besoinAide = VRAI;
      }

      if ( !strcmp(argv[i], "-v") ) {
         sprintf( message, "Mode \"verbose\"" );
         verbose = VRAI;
         besoinAide = FAUX;
      }

      if ( !strcmp(argv[i], "-N") ) {
         if ( (++j < argc) && sscanf(argv[j], "%d", & nbIter) && (nbIter > 0) && (nbIter <= MAX_TIRAGES) ) {
            sprintf( message, "Nombre d'iterations ou de realisations = %d", nbIter );
            besoinAide = FAUX;
         }
         else {
            sprintf( message, "Valeur associee a l'option -N manquante ou invalide\nUsage :" );
            besoinAide = VRAI;
         }
      }

      if ( !strcmp(argv[i], "-S") ) {
         if ( (++j < argc) && sscanf(argv[j], "%d", & germe) && (germe >= 0) ) {
            sprintf( message, "Germe du generateur pseudo-aleatoire = %d%s", germe, (germe == 0) ? " (automatique)" : "" );
            besoinAide = FAUX;
         }
         else {
            sprintf( message, "Valeur associee a l'option -S manquante ou invalide\nUsage :" );
            besoinAide = VRAI;
         }
      }

      if ( !strcmp(argv[i], "-EXO_1") ) {
         switch ( numExo ) {
            case 0 :    sprintf( message, "Execution du code correspondant au 1er exercice" );
                        besoinAide = FAUX;
                        numExo = 1;
                        break;
            case 1 :    sprintf( message, "Option deja selectionnee" );
                        besoinAide = FAUX;
                        break;
            default :   sprintf( message, "Impossible : l'exercice EXO_%d a deja ete choisi\nUsage :", numExo );
                        besoinAide = VRAI;
         } /* switch */
      }

      if ( !strcmp(argv[i], "-EXO_2") ) {
         switch ( numExo ) {
            case 0 :    sprintf( message, "Execution du code correspondant au 2eme exercice" );
                        besoinAide = FAUX;
                        numExo = 2;
                        break;
            case 2 :    sprintf( message, "Option deja selectionnee" );
                        besoinAide = FAUX;
                        break;
            default :   sprintf( message, "Impossible : l'exercice EXO_%d a deja ete choisi\nUsage :", numExo );
                        besoinAide = VRAI;
         } /* switch */
      }

      if ( !strcmp(argv[i], "-EXO_3") ) {
         switch ( numExo ) {
            case 0 :    sprintf( message, "Execution du code correspondant au 3eme exercice" );
                        besoinAide = FAUX;
                        numExo = 3;
                        break;
            case 3 :    sprintf( message, "Option deja selectionnee" );
                        besoinAide = FAUX;
                        break;
            default :   sprintf( message, "Impossible : l'exercice EXO_%d a deja ete choisi\nUsage :", numExo );
                        besoinAide = VRAI;
         } /* switch */
      }


      /* --- Options des exercices 1 & 2 --- */

      if ( !strcmp(argv[i], "-C") && ((numExo == 1) || (numExo == 2)) ) {
         if ( (++j < argc) && sscanf(argv[j], "%d", & nbClasses) && (nbClasses > 0) ) {
            sprintf( message, "Nombre de classes de l'histogramme = %d", nbClasses );
            besoinAide = FAUX;
         }
         else {
            sprintf( message, "Valeur associee a l'option -C manquante ou invalide\nUsage :" );
            besoinAide = VRAI;
         }
      }


      /* --- Options de l'exercice 3 --- */

      if ( !strcmp(argv[i], "-d") && (numExo == 3) ) {
         sprintf( message, "Affichage des points" );
         disPoints = VRAI;
         besoinAide = FAUX;
      }

      printf( "\t%s\t%s\n", argv[i], message );
      i = j;

   } /* for */


   /* --- Lancement des fonctions de traitement --- */

   if ( verbose ) putchar( '\n' );

   if ( ! besoinAide )
      switch ( numExo )
      {

         case 1 :    exo1( nbIter, germe, nbClasses );
                     break;
         case 2 :    exo2( nbIter, germe, nbClasses );
                     break;
         case 3 :    exo3( nbIter, germe );
                     break;
         default :   printf( "\tAucun numero d'exercice n'a ete selectionne\nUsage :\n" );
                     besoinAide = VRAI;

      } /* switch */


   /* --- Affichage de l'aide si besoin --- */

   putchar( '\n' );
   if ( besoinAide )
      aide( argv[0] );
   putchar( '\n' );


   return EXIT_SUCCESS;

}


/* === Fonctions fournies ======================================================================= */

void aide( char * nomComm )
{

   char      * chaine = strrchr( nomComm, '/' );


   chaine = ( chaine == NULL ) ? nomComm : chaine + 1;

   printf( B_ON "NOM\n" B_OFF, ESC, ESC );
   printf( "\t%s - TP d'algorithmique - Algos et tirages aleatoires\n\n", chaine );

   printf( B_ON "SYNOPSIS\n" B_OFF, ESC, ESC );
   printf( "\t" B_ON "%s" B_OFF " [EXO_numero] [OPTIONS_DE_L'EXO]...\n\n", ESC, chaine, ESC );

   printf( B_ON "DESCRIPTION\n\n" B_OFF, ESC, ESC );
   printf( "\t%s\t\tAffiche ce message d'aide\n", chaine );
   printf( "\t%s " B_ON "-h" B_OFF "\tAffiche ce message d'aide\n", chaine, ESC, ESC );
   printf( "\t%s " B_ON "-help" B_OFF "\tAffiche ce message d'aide\n\n", chaine, ESC, ESC );
   printf( "\t%s " B_ON "-EXO_1" B_OFF " [OPTS]...\tExec. fonction exercice 1\n", chaine, ESC, ESC );
   printf( "\t%s " B_ON "-EXO_2" B_OFF " [OPTS]...\tExec. fonction exercice 2\n", chaine, ESC, ESC );
   printf( "\t%s " B_ON "-EXO_3" B_OFF " [OPTS]...\tExec. fonction exercice 3\n\n", chaine, ESC, ESC );

   printf( B_ON "OPTIONS GENERALES\n\n" B_OFF, ESC, ESC );
   printf( "\t" B_ON "-v" B_OFF "\t\tMode \"verbose\" (%s par defaut) : affiche des informations supplementaires sur le deroulement des algorithmes (donnees ...)\n\n", ESC, ESC, (vbDef) ? "active" : "absent" );
   printf( "\t" B_ON "-N" B_OFF " entier>0\tNombre de realisations de l'experience (valeur par defaut = %d) : nombre de tirages aleatoires (<= %d) ou d'iterations\n\n", ESC, ESC, nbiDef, MAX_TIRAGES );
   printf( "\t" B_ON "-S" B_OFF " entier>=0\tGerme (seed) pour initialisation du generateur pseudo-aleatoire (automatique S = 0, valeur par defaut)\n\n", ESC, ESC );

printf( B_ON "OPTION EXERCICES 1 & 2\n\n" B_OFF, ESC, ESC );
printf( "\t" B_ON "-C" B_OFF " entier>0\tNombre de classes pour le calcul de l'histogramme (valeur par defaut = %d)\n\n", ESC, ESC, nbClassesDef );

printf( B_ON "OPTION EXERCICE 3\n\n" B_OFF, ESC, ESC );
printf( "\t" B_ON "-d" B_OFF "\t\tAffichage des points dans la fenetre graphique en cours de calcul (%s par defaut) : desactiver pour accelerer le calcul avec un grand nombre de tirages\n\n", ESC, ESC, (dpDef) ? "active" : "absent" );

}


void exo1( int nbTir, unsigned int seed, int nbClasses )
{

   double          * data = (double *) calloc( nbTir, sizeof(double) );
   double          * intervalle = (double *) calloc( nbClasses + 1, sizeof(double) );
   int             * hist = (int *) calloc( nbClasses, sizeof(int) );

   CImg<int>         imHist;
   CImgDisplay       affHist;

   double            total = 0.;
   int               i;


   if ( seed == 0 )                                      /* Bonne strategie par defaut, pour la */
      seed = time( NULL );                               /* selection d'un germe quelconque     */

   tirageUniforme( seed, nbTir, data );
   if ( verbose ) {
      puts( "Donnees generees :" );
      for ( i = 0; i < nbTir; ++i )
         printf( "%lf\n", data[i] );
   }

   histogramme( data, nbTir, 0., 1., nbClasses, intervalle, hist );
   if ( verbose ) {
      for ( i = 0; i < nbClasses; ++i )
         total += hist[i];
      printf( "\nTotal histogramme :\n%f\n", total );
   }

   affHist.assign( imHist.assign(hist, nbClasses), "Histogramme" ).resize( 640, 480 ).move( 350, 250 );
   imHist.display_graph( affHist, 3, 0, "Support valeurs aleatoire", 0., 1., "Effectifs", 0, 1.05*imHist.max() );


   free( data );
   free( intervalle );
   free( hist );

}


void exo2( int nbTir, unsigned int seed, int nbClasses )
{

   int                  nbEch = 1000;
   double               xMin = -5, xMax = 5;
   double               step = (xMax - xMin)/(nbEch-1);
   double               m = 0, s = 1;

   double             * x  = (double *) calloc( nbEch, sizeof(double) );
   double             * fx = (double *) calloc( nbEch, sizeof(double) );
   double             * Fx = (double *) calloc( nbEch, sizeof(double) );

   double               mini, maxi;
   double               total = 0.;

   double             * tirageUnif = (double *) calloc( nbTir, sizeof(double) );
   double             * tirageGauss = (double *) calloc( nbTir, sizeof(double) );
   double             * intervalle = (double *) calloc( nbClasses + 1, sizeof(double) );
   int                * hist = (int *) calloc( nbClasses, sizeof(int) );

   CImg<double>         imf, imF;
   CImg<unsigned char>  imCourbes, imCourbes2;
   CImgDisplay          affCourbes, affCourbes2;
   unsigned char        rouge[] = { 255, 0, 0 };

   CImg<int>            imHist;
   CImgDisplay          affHist;

   double               val;
   int                  i;


   val = xMin;
   for ( i = 0; i < nbEch; ++i ) {
      x[i] = val; val += step;
      fx[i] = 1/( s*sqrt(2*M_PI) ) * exp( -0.5*( (x[i]-m)/s )*( (x[i]-m)/s ) );
   }

   imf.assign( fx, nbEch );
   mini = imf.min(); maxi = imf.max();
   imCourbes.assign( 640, 480, 1, 3 );
   cimg_forXY( imCourbes, x, y ) imCourbes.fillC( x, y, 0, 255, 255, 255 );
   imCourbes.draw_graph( imf, rouge, 1., 1, 0, 1.05*maxi, mini-0.05*maxi );
   affCourbes.assign( imCourbes, "Distribution gaussienne" ).move( 350, 250 );

   fRepart( fx, nbEch, step, Fx );

   imF.assign( Fx, nbEch );
   mini = imF.min(); maxi = imF.max();
   imCourbes2.assign( 640, 480, 1, 3 );
   cimg_forXY( imCourbes2, x, y ) imCourbes2.fillC( x, y, 0, 255, 255, 255 );
   imCourbes2.draw_graph( imF, rouge, 1., 1, 0, 1.05*maxi, mini-0.05*maxi );
   affCourbes2.assign( imCourbes2, "Fonction de repartition" ).move( 380, 280 );

   if ( seed == 0 )
      seed = time( NULL );                               /* Selection d'un germe quelconque */

   tirageUniforme( seed, nbTir, tirageUnif );
   tirageAlea( tirageUnif, nbTir, x, Fx, nbEch, tirageGauss );
   histogramme( tirageGauss, nbTir, xMin, xMax, nbClasses, intervalle, hist );
   if ( verbose ) {
      for ( i = 0; i < nbClasses; ++i )
         total += hist[i];
      printf( "Total histogramme :\n%f\n", total );
   }

   affHist.assign( imHist.assign(hist, nbClasses), "Histogramme" ).resize( 640, 480 ).move( 410, 310 );
   imHist.display_graph( affHist, 3, 0, "Support valeurs aleatoire", xMin, xMax, "Effectifs", 0, 1.05*imHist.max() );
   while ( !affCourbes.is_closed() || !affCourbes2.is_closed() )
      affCourbes.wait_all();


   free( x );
   free( fx );
   free( Fx );
   free( tirageUnif );
   free( tirageGauss );
   free( intervalle );
   free( hist );

}


void exo3( int nbTir, unsigned int seed )
{

   int                  size = 350;
   unsigned char        rouge[] = { 255, 0, 0 };
   unsigned char        bleu[] = { 0, 0, 255 };

   double               evalPi;
   double             * values = (double *) calloc( nbTir, sizeof(double) );

   CImg<double>         imCourbe;
   CImgDisplay          affCourbe;


   if ( seed == 0 )
      seed = time( NULL );                               /* Selection d'un germe quelconque */

   imCarre.assign( 350, 350, 1, 3 );
   affCarre.assign( imCarre, "Pi par Monte-Carlo" );

   cimg_forXY( imCarre, x, y ) imCarre.fillC( x, y, 0, 255, 255, 255 );
   imCarre.draw_circle( -1, size, size, rouge, 1., 0 );
   imCarre.draw_line( 0, 0, 0, size-1, bleu );
   imCarre.draw_line( 0, size-1, size-1, size, bleu );
   imCarre.draw_line( size-1, size-1, size-1, 0, bleu );
   imCarre.draw_line( size-1, 0, 0, 0, bleu );
   imCarre.display( affCarre );
   affCarre.move( 500, 300 );

   evalPi = piMC( seed, nbTir, values );
   printf( "\nEvaluation finale de pi :\n%lf\n", evalPi );

   while ( ! affCarre.is_closed() )
      affCarre.wait();

   affCourbe.assign( imCourbe.assign(values, nbTir), "Evolution de l'estimation de pi" ).resize( 640, 480 ).move( 350, 250 );
   imCourbe.display_graph( affCourbe, 1, 0, "Iterations", 1., nbTir, "Estimation de pi", 0.95*imCourbe.min(), 1.05*imCourbe.max() );


   free( values );

}


void histogramme( double donnees[], int nbTir, double minSupport, double maxSupport, int nbClasses,
                  double bornes[], int hist[] )
{

   int         i, j;
   double      step, borne;


   step = ( maxSupport - minSupport )/nbClasses;         /* Nb intervalles => Nb+1 bornes : no   */
                                                         /* problem, l'allocation du tableau est */
                                                         /* adaptee, dans la fonction appelante  */

   /* --- Calcul des intervalles pour repartir les valeurs --- */

   borne = minSupport; i = 0;
   while ( borne < maxSupport ) {                        /* On peut aussi parcourir en i, mais il */
      bornes[i++] = borne;                               /* faut penser à incrementer les deux    */
      borne += step;
   }
   bornes[nbClasses] = maxSupport + EPSILON;             /* Pour corriger d'éventuelles erreurs */
                                                         /* d'arrondi, et assurer le cas peu    */
                                                         /* probable donnees[i] == maxSupport   */
   /* --- Calcul de l'histogramme --- */

   for ( j = 0; j < nbClasses; ++j ) hist[j] = 0;        /* Toujours initialiser, meme si ici  */
                                                         /* c'est fait implicitement a l'appel */
   for ( i = 0; i < nbIter; ++i )
   {

      for ( j = 0; j < nbClasses; ++j )                  /* Tests valeur dans l'intervalle */
         if ( (donnees[i] >= bornes[j]) && (donnees[i] < bornes[j+1]) )
            hist[j]++;                                   /* Nb intervalles => Nb+1 bornes  */

   } /* for */

}


void fRepart( double v_f[], int nbVal, double delta, double v_F[] )
{

   int         i;


   v_F[0] = 0;                                           /* Par hypothese (energie finie).    */
                                                         /* Intervalle support suppose adapte */
   for ( i = 1; i < nbVal; ++i )                         /* On calcule une somme cumulee */
      v_F[i] = v_F[i-1] + v_f[i]*delta;                  /* Integration numerique des rectangles */
                                                         /*  => somme surfaces elementaires      */
}


void tracePoint( double x, double y, unsigned char forme )
{

   unsigned char     rouge[] = { 255, 0, 0 };
   unsigned char     bleu[] = { 0, 0, 255 };
   int               width = imCarre.width();
   int               xc = (int) ( x*(width-1) );
   int               yc = (int) ( y*(width-1) );


   switch ( forme )
   {

      case 'o' : imCarre.draw_circle( xc, (width-1)-yc, 3, bleu );
                 if ( disPoints ) imCarre.display( affCarre );
                 break;
      case 's' : imCarre.draw_rectangle( xc-4, (width-1)-(yc-4), xc+4, (width-1)-(yc+4), rouge );
                 if ( disPoints ) imCarre.display( affCarre );
                 break;
      /* default = rien */

   } /* switch */

}

/* ********************************************************************************************** */
/* *** Procedures and functions to be completed ************************************************* */
/* ********************************************************************************************** */


/* === 1. Uniform random draw =================================================================== */

/* -------------------------------------------------------------------- */
/* Tirage uniforme d'un ensemble de valeurs                             */
/* Entrees :   seed     Germe d'initialisation du generateur            */
/*                      pseudo-aleatoire                                */
/*             nbTir    Nombre de valeurs à generer                     */
/* E/S :       donnees  Collection de donnees generees                  */
/*                      (tableau pre-alloue)                            */
/* -------------------------------------------------------------------- */

void tirageUniforme( unsigned int seed, int nbTir, double donnees[] )
{
	int i;
	srand(seed);
	
	for ( i = 0; i < nbTir; ++i) {
		donnees[i] = ((double) rand())/RAND_MAX;
	}
}


/* === 2. Inverse transform sampling ============================================================= */

/* -------------------------------------------------------------------- */
/* Tirage d'un ensemble de valeurs selon une loi donnee                  */
/* Entrees :   d_Unif      Donnees tirees selon une loi uniforme        */
/*             nbTir       Nombre de tirages aleatoires                 */
/*             support     Position des echantillons de la fonction F   */
/*             v_F         Echantillons de la fonction de repartition F */
/*             nbVal       Nombre de valeurs dans support et v_F        */
/* E/S :       donnees     Collection de donnees generees               */
/*                         (tous les tableaux sont pre-allouex)         */
/* -------------------------------------------------------------------- */

void tirageAlea( double d_Unif[], int nbTir, double support[], double v_F[], int nbVal,
                 double donnees[] )
{
	
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

	/*
	int i, j, j_point;
	double u, closest, x;

	for (i = 0; i < nbTir; i ++) {
		u = d_Unif[i];
		closest = v_F[0];
		j_point = 0;
		for (j = 0; j < nbVal; j ++) {
			if (fabs(v_F[j] - u) < closest) {
				closest = v_F[j];
				j_point = j;
			}
		}
		x = support[j];
		donnees[i] = x;
	}*/
}


/* === 3. Estimation of pi using the Monte-Carlo method ============================================ */

/* -------------------------------------------------------------------- */
/* Calcul de pi par methode de Monte-Carlo                              */
/* Entrees :   seed     Germe d'initialisation du generateur            */
/*                      pseudo-aleatoire                                */
/*             nbTir    Nombre de tirages aleatoires                    */
/* E/S :       valeurs  Estimations successives de la valeur de pi      */
/*                      (tableau pre-alloue)                            */
/* -------------------------------------------------------------------- */

double piMC( unsigned int seed, int nbTir, double valeurs[] )
{
	/*
	Generate one by one the indicated pairs of random values from uniform distributions 
	that correspond to the x and y coordinates of the points.

	If the resulting point is inside the pre-defined circular section draw it with 
	a square (tracePoint(x, y, 's') and update accordingly the pi value estimation.

	If the resulting point is outside the pre-defined circular section draw it with 
	a circle (tracePoint(x, y, 'o') and update accordingly the pi value estimation.

	Return the estimated value of pi after all the generated pairs of random points
        have been tested (to verify if the point is inside or outside the pre-defined 
        circular section).
	*/

	double      pi = 0.;
	double      x, y;
	int         in;  /* in = points inside the circular area */
	int         all; /* all = total number of drawn points */
	int         i;

	srand( seed );                                                                                       

	in = 0;
	all = 0;   

	for ( i = 0; i < nbTir; ++i) {
		x = ((double) rand())/RAND_MAX;
		y = ((double) rand())/RAND_MAX;

		if ((x * x + y * y) <= 1) {
			tracePoint(x, y, 's');
			in ++;
		} else {
			tracePoint(x, y, 'o');
		}
		all ++;
			
		pi = ((double)in / (double)all) * 4;
		valeurs[i] = pi;
	}
	return pi;
}

