package squelette;

import java.util.Map;

public abstract class AefV2 {
	
	private int etat;
	private int[] terminal_state;
	private Map<Character, Integer> table_transition;
	
	public AefV2 (int etat_initial, int[] etats_terminaux, Map<Character, Integer> table_transition){
		etat = etat_initial;
		terminal_state = etats_terminaux;
		this.table_transition = table_transition;
	}
	
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
		if (isTerminal(etat)) return true; // entree est acceptee
		else return false; // entree n'est pas acceptee
	};
	
	public abstract int transition (int etatCourant, char symboleLu) {
		
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
