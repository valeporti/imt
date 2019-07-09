package squelette;

/**
 * Aef1 est un automate reconnaissant le langage des mots de la forme 
 * 
 * @author cousin
 *
 */
public class Aef2tt extends Aef {
	
	private int etat;
	private int[] terminal_state;
	
	public Aef2tt (int etat_initial, int[] etats_terminaux){
		etat = etat_initial;
		terminal_state = etats_terminaux;
	}

	@Override
	public boolean accepte(String entree) {
		int etat = initial (); // etat initial de l'automate
		int index = 0; // rang du premier caractere a traiter
		char carlu; // caractere courant
		
		while(index != entree.length()) {
			// tant qu'il reste des caracteres a traiter
			carlu = entree.charAt(index++); // lecture caractere courant et passage au suivant
			
			etat = transition(etat, carlu);
			if (etat < 0) return false;
		}
		
		// il n'ya plus rien a lire : est-on dans un etat terminal ?
		return isTerminal(etat);
	}
	
	private int transition (int etatCourant, char symboleLu){
		
		if ((etatCourant==0)&&(symboleLu=='a')) return 1;
		else if ((etatCourant == 1) && (symboleLu=='b')) return 2;
		else if ((etatCourant == 2) && (symboleLu=='b' || symboleLu=='a')) return 3;
		else if ((etatCourant == 3) && (symboleLu=='b')) return 4;
		else if ((etatCourant == 3) && (symboleLu=='a')) return 3;
		else if ((etatCourant == 4) && (symboleLu=='b')) return 4;
		else if ((etatCourant == 4) && (symboleLu=='a')) return 5;
		else if ((etatCourant == 5) && (symboleLu=='b')) return 4;
		else if ((etatCourant == 5) && (symboleLu=='a')) return 3;
		else return -1;
		
	}
	
	private boolean isTerminal (int etat){
		for (int ele: terminal_state) {
			if (ele == etat) return true;
		}
		return false;
	}
	
	private int initial (){
		return this.etat;
	}

}