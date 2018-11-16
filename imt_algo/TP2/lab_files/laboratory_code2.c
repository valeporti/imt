/* ********************************************************************************************** */
/* UVMSC-INF101A: Algorithms                                                                 */
/* Laboratory 2: Complexity of sorting algorithms                                                         */
/* Adapted from Philippe Lenca et Julien Montagner                                                             */
/* Version 2.1                                                                                    */
/* ********************************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>


/* Type des donnees a trier */
#define UNKNOW  0
#define FICHIER 1
#define RANDOM  2
#define TRIE    3
#define TRIE_INVERSE 4


/* Type de tri a utiliser */
/* Numero XY, X pour la famille, Y pour la version */
#define BULLE_NAIF 11
#define BULLE_OPT  12
#define SELECTION  2
#define INSERTION  3


/* Divers */
#define TRUE 1
#define FALSE 0


/* Elements d'analyse mesures */
typedef struct
{
  long long nb_copies;          /* entiers 64 bits pour les cas > 1E5 valeurs */
  long long nb_echanges;
  long long nb_comparaisons;
} complexiteDef;


/* Prototypes des fonctions */

/* Afficher l'aide */
int aide(char *nom);

/* Lire les donnees a trier dans un fichier */
int *f_lire_data(char *, int *);

/* Ecrire les donnees dans un fichier */
int f_ecrire_data(char *, int *t, int );

/* Creer des donnees deja triees */
int *data_triee(int *t, int n);

/* Creer des donnees triees dans l'ordre inverse */
int *data_triee_inverse(int *t, int n);

/* Creer des donnees aleatoirement */
int *random_data(int *t, int n);

/* Ecrire les donnees dans le terminal */
int ecrire_data(int *t, int );

/* Ecrire le nombre de comparaisons et d'echanges */
int analyse_complexite(complexiteDef *complexite, char *tri);

/* Echanger deux elements d'un tableau */
void echanger(int *t, int n1, int n2);

/* Algorithmes de tris */
int tri_selection(int *, int, complexiteDef *);
/*int tri_bulle_opt(int *, int, complexiteDef *);*/
int tri_insertion(int *, int, complexiteDef *);
int tri_bulle_naif(int *, int, complexiteDef *);




/* -------------------------------------------------------------------------- */
/* f_lire_data                                                                */
/* int *f_lire_data(char *fichier, int *n)                                    */
/*                                                                            */
/* Lit les elements de type entier dans le fichier texte de nom [file]        */
/*                                                                            */
/* Entrees :                                                                  */
/*   - [file]    : nom du fichier texte contenant les donnees entieres        */
/*                 premiere ligne   : nombre [n] d'elements a lire            */
/*                 lignes suivantes : les [n] entiers a lire                  */
/* Modifications :                                                            */
/*   - [n]       : nombre entier d'elements a lire                            */
/*                                                                            */
/* Sorties :                                                                  */
/*   - [tab]      : tableau de type int ou sont stockes les entiers lus       */
/* -------------------------------------------------------------------------- */


int *f_lire_data(char *fichier, int *n)
{
  int i;
  FILE *f;
  int *tab;

  /* Ouverture du fichier en lecture */
  f = fopen(fichier, "rt");
  if (f == NULL)
    {
      printf("\n\nOuverture du fichier %s impossible\n\n", fichier);
      return 0;
    }


  /* Lecture du nombre d'elements a lire */
  fscanf (f, "%d\n", n);


  /* Allocation de la memoire necessaire */
  tab = (int *) calloc(*n, sizeof(int));

  /* Lecture des n elements */
  for (i = 0; i < *n; i++)
    fscanf (f, "%d\n", &tab[i]);

  fclose(f);
  return(tab);
}


/* -------------------------------------------------------------------------- */
/* f_ecrire_data                                                              */
/* int f_ecrire_data(char *fichier, int *t, int n)                            */
/*                                                                            */
/* Ecrire les [n] elements de type entier du tableau [t] dans un fichier de   */
/* type texte de nom [fichier]                                                */
/*                                                                            */
/* Entrees :                                                                  */
/*   - [fichier] : nom du fichier                                             */
/*   - [t] : tableau d'entiers                                                */
/*   - [n] : nombre d'entiers du tableau                                      */
/*                                                                            */
/* Sorties :                                                                  */
/*   - [n] : nombre d'entiers du tableau                                      */
/* -------------------------------------------------------------------------- */

int f_ecrire_data(char * fichier, int *t, int n)
{
  FILE *f;
  int i;

  /* Ouverture du fichier en ecriture*/
  f = fopen(fichier, "wt");
  if (f == NULL)
    {
      printf("\n\nEcriture <f_ecrire_data> :\n");
      printf("Ouverture du fichier %s impossible\n\n", fichier);
      return 0;
    }

  fprintf(f, "%d\n", n);

  for (i = 0; i < n; i++)
    fprintf(f, "%d\n", t[i]);

  fclose(f);
  return n;
}


/* -------------------------------------------------------------------------- */
/* ecrire_data                                                                */
/* int ecrire_data(int *t, int n)                                             */
/*                                                                            */
/* Ecrire les [n] elements de type entier du tableau [t]                      */
/*                                                                            */
/* Entrees :                                                                  */
/*   - [t] : tableau d'entiers                                                */
/*   - [n] : nombre d'entiers du tableau                                      */
/*                                                                            */
/* Sorties :                                                                  */
/*   - [n] : nombre d'entiers du tableau                                      */
/* -------------------------------------------------------------------------- */

int ecrire_data(int *t, int n)
{
  int i;

  printf("\n");
  for (i = 0; i < n; i++)
    printf("%d\n", t[i]);
  printf("\n");
  return n;
}


/* -------------------------------------------------------------------------- */
/* random_data                                                                */
/* int *random_data(int *t, int n)                                            */
/*                                                                            */
/* Creer [n] nombres entiers aleatoires, les stocker dans le tableau [t]      */
/*                                                                            */
/*                                                                            */
/* Entrees :                                                                  */
/*   - [t] : tableau d'entiers                                                */
/*   - [n] : nombre d'entiers du tableau                                      */
/*                                                                            */
/* Modifications :                                                            */
/*   - [t] : tableau d'entiers                                                */
/*                                                                            */
/* Sorties :                                                                  */
/*   - [t] : tableau d'entiers                                                */
/* -------------------------------------------------------------------------- */


int *random_data(int *t, int n)
{
  int i;
  int pid;

  pid = getpid ();
  srand(pid);

  t = (int *) calloc(n, sizeof(int));

  for (i = 0; i < n; i++)
    t[i]  = 1+(int) ((double) n *rand()/(RAND_MAX+1.0));

  return t;
}

/* -------------------------------------------------------------------------- */
/* data_triee                                                                 */
/* int *data_triee(int *t, int n)                                             */
/*                                                                            */
/* Idem a random pour les entrees, sorties mais le tableau [t] contient les   */
/* [n] premiers entiers dans l'ordre sans ex-aequo.                           */
/* -------------------------------------------------------------------------- */

int *data_triee(int *t, int n)
{
  int i;

  t = (int *) calloc(n, sizeof(int));

  for (i = 0; i < n; i++)
    t[i]  = i;

  return t;
}
/* -------------------------------------------------------------------------- */
/* data_triee_inverse                                                         */
/* int *data_triee_inverse(int *t, int n)                                     */
/*                                                                            */
/* Idem a random pour les entrees, sorties mais le tableau [t] contient les   */
/* [n] premiers entiers dans l'ordre inverse sans ex-aequo.                   */
/* -------------------------------------------------------------------------- */

int *data_triee_inverse(int *t, int n)
{
  int i;

  t = (int *) calloc(n, sizeof(int));

  for (i = 0; i < n; i++)
    t[n-1-i]  = i;

  return t;
}


int analyse_complexite(complexiteDef *complexite, char *tri)
{
  printf("\nAnalyse de la complexite du tri %s\n", tri);
  printf("\n  nombre de copies       = %lld\n", complexite->nb_copies);
  printf("\n  nombre d'echanges      = %lld\n", complexite->nb_echanges);
  printf("\n  nombre de comparaisons = %lld\n", complexite->nb_comparaisons);
  return 0;
}



/* -------------------------------------------------------------------------- */
/* aide                                                                       */
/* int aide(char * nom)                                                       */
/*                                                                            */
/* Afficher les differentes options du programme [nom]                        */
/*                                                                            */
/* Entrees :                                                                  */
/* Modifications :                                                            */
/* Sorties :                                                                  */
/* -------------------------------------------------------------------------- */


int aide(char *nom)
{
  printf("\nUtilisation :\n\n  %s [options]\n", nom);
  printf("\n");
  printf("\nOptions :\n");
  printf("\n  - pour afficher ou non les tableaux : - v (afficher) (par defaut on n'affiche pas)\n");
  printf("\n[1] Pour les donnees (des entiers) :\n");
  printf("\n  - lues dans un Fichier texte : -f [nom_fichier]\n");
  printf("\n    ou [nom_fichier] est le nom d'un fichier texte de la forme\n");
  printf("\n      nombre_elements");
  printf("\n      entier1");
  printf("\n      entier2");
  printf("\n      ...");
  printf("\n      entiern");
  printf("\n");
  printf("\n   - crees Aleatoirement : -a [nombre entier]");
  printf("\n");
  printf("\n   - deja triees (Meilleur des Cas) : -mc [nombre entier]");
  printf("\n");
  printf("\n   - triees dans l'ordre inverse (Pire des Cas) : -pc [nombre entier]");
  printf("\n");
  printf("\n   - pour les Sauver dans un fichier texte : -s [nom_fichier]");
  printf("\n");
  printf("\n[2] Pour l'algorithme de Tri : -t [algo]\n");
  printf("\n    ou [algo] = selection, insertion, bulle_naif\n");
  printf("\n");
  printf("\nExemples :\n");
  printf("\n  donnees lues dans le fichier tab1.dat et triees avec bulle");
  printf("\n    -f tab1.dat -t bulle_naif\n");
  printf("\n    -t bulle_naif -f tab1.dat\n");
  printf("\n  10 donnees crees aleatoirement et triees avec insertion");
  printf("\n    -a 10 -t insertion\n");
  printf("\n    -t insertion -a 10\n");
  printf("\n  8 donnees dans l'ordre inverse, triees avec selection, sauvees dans tab1.dat");
  printf("\n    -pc 8 -t selection -s tab1.dat\n");
  printf("\n");
  return 0;
}





/* -------------------------------------------------------------------------- */

int main(int argn, char *argv[])
{
  int type_data;
  int type_tri;
  int sauvegarde;
  int type_sortie_terminal;

  int n;
  char *fichier, *fichierSauv;
  int *tab = NULL;
  int i;

  complexiteDef *complexite;

  if (argn == 1)
    return aide(argv[0]);

  type_data = UNKNOW;
  type_tri = UNKNOW;
  sauvegarde = UNKNOW;
  type_sortie_terminal = FALSE;

  for ( i = 1; i < argn; i++ )
    {

      if (strcmp("-f", argv[i]) == 0)
	{
	  fichier = (char *) malloc(1 + strlen(argv[i+1]) * sizeof(char));
	  strcpy(fichier, argv[i+1]);
	  type_data = FICHIER;
	}

      if (strcmp("-s", argv[i]) == 0)
	{
	  fichierSauv = (char *) malloc(1 + strlen(argv[i+1]) * sizeof(char));
	  strcpy(fichierSauv, argv[i+1]);
	  sauvegarde = FICHIER;
	}

      if (strcmp("-a", argv[i]) == 0)
	{
	n = atoi(argv[i+1]);
	type_data = RANDOM;
	}

      if (strcmp("-mc", argv[i]) == 0)
	{
	  n = atoi(argv[i+1]);
	  type_data = TRIE;
	}

      if (strcmp("-pc", argv[i]) == 0)
	{
	  n = atoi(argv[i+1]);
	  type_data = TRIE_INVERSE;
	}



      if (strcmp("-t", argv[i]) == 0)
	{
	  if (strcmp("bulle_naif", argv[i+1]) == 0)
	    type_tri = BULLE_NAIF;

	  if (strcmp("bulle_opt", argv[i+1]) == 0)
	    type_tri = BULLE_OPT;

	  if (strcmp("selection", argv[i+1]) == 0)
	    type_tri = SELECTION;

	  if (strcmp("insertion", argv[i+1]) == 0)
	    type_tri = INSERTION;
	}

     if (strcmp("-v", argv[i]) == 0)
	{
	type_sortie_terminal = TRUE;
	}
    }

  printf("\n");

  switch(type_data)
    {
    case TRIE:
      {
	tab = data_triee(tab, n);
	printf("Tableau trie (meilleur des cas)");
	/* ecrire_data(tab,  n); */
	break;
      }

      case TRIE_INVERSE:
      {
	tab = data_triee_inverse(tab, n);
	printf("Tableau trie ordre inverse (pire des cas)");
	/* ecrire_data(tab,  n); */
	break;
      }
    case FICHIER:
      {
	tab = f_lire_data(fichier, &n);
	printf("Tableau lu dans %s", fichier);
	/* ecrire_data(tab,  n); */
	break;
      }
    case RANDOM:
      {
	printf("Type data %d ", type_data);
	tab = random_data(tab, n);
	printf("Tableau aleatoire");
	/* ecrire_data(tab,  n); */
	break;
      }
    case UNKNOW:
      return aide(argv[0]);
    }


  complexite = (complexiteDef *) malloc(sizeof(complexiteDef));

  if (complexite == NULL)
    {
    printf("\nProbleme d'allocation memoire pour la structure [complexite]\n");
    return 0;
    }

  if (type_sortie_terminal == TRUE) ecrire_data(tab,  n);

  complexite->nb_comparaisons = 0;
  complexite->nb_echanges = 0;
  complexite->nb_copies = 0;

  switch(type_tri)
    {
    case BULLE_NAIF:
      tri_bulle_naif(tab, n, complexite);
      if (type_sortie_terminal == TRUE) {
      	printf("Tableau trie (bulle naif)\n");
      	ecrire_data(tab,  n);
	}
      analyse_complexite(complexite, "bulle naif");
      break;
    /*case BULLE_OPT:
      tri_bulle_opt(tab, n, complexite);
      if (type_sortie_terminal == TRUE) {
      	printf("Tableau trie (bulle optimise)\n");
      	ecrire_data(tab,  n);
	}
      analyse_complexite(complexite, "bulle optimise");
      break;*/
    case SELECTION:
      tri_selection(tab, n, complexite);
      if (type_sortie_terminal == TRUE) {
        printf("Tableau trie (selection)\n");
        ecrire_data(tab,  n);
	}
      analyse_complexite(complexite, "selection");
      break;
    case INSERTION:
      tri_insertion(tab, n, complexite);
      if (type_sortie_terminal == TRUE) {
      	printf("Tableau trie (insertion)\n");
      	ecrire_data(tab,  n);
	}
      analyse_complexite(complexite, "insertion");
      break;
    case UNKNOW:
      return aide(argv[0]);
    }


  if (sauvegarde == FICHIER)
    f_ecrire_data(fichierSauv, tab, n);

  printf("\n");
  return 0;
}





/* -------------------------------------------------------------------------- */
/* echanger                                                                   */
/* void echanger(int *t, int n1, int n2)                                      */
/*                                                                            */
/* Echanger les elements d'indice [n1] et [n2] du tableau d'entiers [t]       */
/*                                                                            */
/* Entrees :                                                                  */
/*   - [t]  : tableau d'entiers                                               */
/*   - [n1] : indice                                                          */
/*   - [n2] : indice                                                          */
/*                                                                            */
/* Modifications :                                                            */
/*   - [t]  : tableau d'entiers                                               */
/*                                                                            */
/* Sorties :                                                                  */
/*   - void                                                                   */
/* -------------------------------------------------------------------------- */

void echanger(int *t, int n1, int n2)

{
  int inter;

  inter = t[n1];
  t[n1] =  t[n2];
  t[n2] = inter;
}



/* -------------------------------------------------------------------------- */
/* tri_[algo_tri]                                                             */
/* int tri_[algo_tri] (int *t, int n, complexiteDef *complexite)              */
/*                                                                            */
/* Trier le tableau d'entiers [t] a [n] elements                              */
/* [algo_tri] : selection, insertion, bulle_naif                              */
/*                                                                            */
/* Entrees :                                                                  */
/*   - [t] : tableau d'entiers                                                */
/*   - [n] : nombre d'entiers du tableau                                      */
/*                                                                            */
/* Modifications :                                                            */
/*   - [t] : tableau d'entiers                                                */
/*                                                                            */
/*   - [complexite] : complexite                                              */
/*            complexite->nb_copies                                     */
/*            complexite->nb_comparaisons                                     */
/*            complexite->nb_echanges                                         */
/* -------------------------------------------------------------------------- */


/* -------------------------------------------------------------------------- */
/* -------------------------------------------------------------------------- */
/* ------------------ F U N C T I O N S  T O  C O M P L E T E --------------- */
/* -------------------------------------------------------------------------- */
/* -------------------------------------------------------------------------- */


/* ------------------------------ SELECTION sort ---------------------------- */
int tri_selection(int *data, int size, complexiteDef *complexite)
{
  

  int i, j, min;

  /* trie */
  for (i = 0; i < size - 1; i ++) {
    min = i;
    complexite->nb_copies ++;
    for (j = i + 1; j <= size - 1; j ++) {
      if(data[j] < data[min]) {
	      min = j;
        complexite->nb_copies ++;
        complexite->nb_comparaisons ++;
      }
      if(min != i) {
	      echanger(data, min, i);   
        min = i;
        complexite->nb_echanges ++;
        complexite->nb_copies += 4;
        complexite->nb_comparaisons ++;
      }
    }
  }
  /* Debugging the function ...
  printf("\n ");
  for (int i = 0; i < size; i ++) {
    printf("%i ", data[i]);
  }
  printf("\n ");
  */

  return 0;
}


/* ------------------------------ INSERTION sort ---------------------------- */
int tri_insertion(int *data, int size, complexiteDef *complexite)
{

  int i, j, v;

  for (i = 1; i < size; i ++) {
    v = data[i];
    j = i;
    complexite->nb_copies += 2;
    while (j > 0 && data[j - 1] > v) {
      data[j] = data[j - 1];
      complexite->nb_copies ++;
      complexite->nb_comparaisons ++;
      j --;
    }
    data[j] = v;
    complexite->nb_copies ++;
  }

  return 0;
}


/* ------------------------------ BUBBLE sort ---------------------------- */
int tri_bulle_naif(int *data, int size, complexiteDef *complexite)
{

  int i, j;

  for (i = size - 1; i >= 1; i --) {
    for (j = 1; j <= i; j ++) {
      if(data[j - 1] > data[j]) {
	      echanger(data, j - 1, j);
        complexite->nb_copies += 3;
        complexite->nb_echanges ++;
        complexite->nb_comparaisons ++;
      }
    }
  }

  return 0;
}

/* typedef struct
{
  long long nb_copies;           entiers 64 bits pour les cas > 1E5 valeurs 
  long long nb_echanges;
  long long nb_comparaisons;
} */

