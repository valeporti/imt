package squelette;

/**
 * Aef1 est un automate reconnaissant le langage des mots de la forme 
 * 
 * @author cousin
 *
 */
public class Aef2 extends Aef {

	@Override
	public boolean accepte(String entree) {
		int etat = 0; // etat initial de l'automate
		int index = 0; // rang du premier caractere a traiter
		char carlu; // caractere courant
		
		while(index != entree.length()) {
			// tant qu'il reste des caracteres a traiter
			carlu = entree.charAt(index++); // lecture caractere courant et passage au suivant
			
			if ((etat==0)&&(carlu=='a')) etat=1;
			else if ((etat == 1) && (carlu=='b')) etat=2;
			else if ((etat == 2) && (carlu=='b' || carlu=='a')) etat=3;
			else if ((etat == 3) && (carlu=='b')) etat=4;
			else if ((etat == 3) && (carlu=='a')) etat=3;
			else if ((etat == 4) && (carlu=='b')) etat=4;
			else if ((etat == 4) && (carlu=='a')) etat=5;
			else if ((etat == 5) && (carlu=='b')) etat=4;
			else if ((etat == 5) && (carlu=='a')) etat=3;
			else return false;
		}
		
		// il n'ya plus rien a lire : est-on dans un etat terminal ?
		if (etat==2 || etat==5) return true; // entree est acceptee
		else return false; // entree n'est pas acceptee
	}

}
