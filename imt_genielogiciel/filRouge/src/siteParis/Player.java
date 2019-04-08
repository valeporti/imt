package siteParis;

import java.util.Collection;
import java.util.LinkedList;
import java.util.UUID;


public class Player extends User {
	
	/**
	 * @uml.property  name="jetonsQuantity"
	 */
	private long jetonsQuantity;
	
	/**
	 * @uml.property   name="paris"
	 * @uml.associationEnd   multiplicity="(0 -1)" inverse="player:siteParis.Pari"
	 */
	private LinkedList<Pari> paris; 

	/**
	 * @uml.property  name="passwordPlayer"
	 */
	private String passwordPlayer;

	/**
	 * constructeur de <code>Player</code>. 
	 * 
	 * @param nom nom du joueur
	 * @param prenom du joueur. 
	 * @param pseudo du joueur. 
	 *  
	 */
	public Player(String nom, String prenom, String pseudo) {
		this.setNom(nom);
		this.setPrenom(prenom);
		this.setPseudo(pseudo);
		this.passwordPlayer = null;
		this.setParis();
	}

	/**
	 * Ajouter des Jetons aux jetons existants
	 * 
	 * @param plus quantité de jetons
	 *  
	 */
	public long addJetons(long plus) {
		long j = this.getJetonsQuantity();
		this.setJetonsQuantity(j + plus);
		return this.getJetonsQuantity();
	}

	/**
	 * Verifier si le joueur est instrit à des paris ouverts à présent
	 *  
	 */
	public boolean parisEnCours() {
		for (Pari p: this.paris) {
			// n'a pas été soldé 
			if (!p.getCompetition().getSolde()) {
				return true;
			}
		}
		return false;
	}
		
	/**
	 * Getter of the property <tt>jetonsQuantity</tt>
	 * @return  Returns the jetonsQuantity.
	 * @uml.property  name="jetonsQuantity"
	 */
	public long getJetonsQuantity() {
		return jetonsQuantity;
	}

	/**
	 * Getter of the property <tt>paris</tt>
	 * @return  Returns the paris.
	 * @uml.property  name="paris"
	 */
	public LinkedList<Pari> getParis() {
		return paris;
	}
	
	/**
	 * Ajouter un Pari associé au joueur
	 * 
	 * @param p Pari
	 *  
	 */
	public void addPari(Pari p) {
		this.paris.add(p);
	}

	/**
	 * Obtenir le password du joueur
	 *  
	 */
	public String getPassword() {
		return passwordPlayer;
	}
	
	/**
	 * Setter of the property <tt>jetonsQuantity</tt>
	 * @param jetonsQuantity  The jetonsQuantity to set.
	 * @uml.property  name="jetonsQuantity"
	 */
	public void setJetonsQuantity(long jetonsQuantity) {
		this.jetonsQuantity = jetonsQuantity;
	}
	
	/**
	 * Setter of the property <tt>paris</tt>
	 * @param paris  The paris to set.
	 * @uml.property  name="paris"
	 */
	public void setParis() {
		this.paris = new LinkedList<Pari>();
	}

	/**
	 * Setter of the property <tt>passwordPlayer</tt>
	 * @uml.property  name="passwordPlayer"
	 */
	public String setPassword() {
		this.passwordPlayer = UUID.randomUUID().toString();
		return this.passwordPlayer;
	}

	/**
	 * Enlever des jetons du joueur
	 * 
	 * @param minus Quantité à enlever
	 *  
	 */
	public long takeOutJetons(long minus) {
		long j = this.getJetonsQuantity();
		this.setJetonsQuantity(j - minus);
		return this.getJetonsQuantity();
	}
	
	/**
	 * Enlister les joueurs en suivant une structure Nom, Prenom, pseudo, jetons, jetons pariés
	 *  
	 */
	public LinkedList<String> getLinkedListPlayer() {
		LinkedList<String> joueur = new LinkedList<String>();
		joueur.add(getNom());
		joueur.add(getPrenom());
		joueur.add(getPseudo());
		joueur.add(Long.toString(getJetonsQuantity()));
		joueur.add(Long.toString(getJetonsInParis()));
		return joueur;
	}
	
	/**
	 * Obtenir si jamais, il y a des jetons dans des paris pas soldés
	 * 
	 */
	public long getJetonsInParis() {
		long total = 0;
		for (Pari p: this.getParis()) {
			if (!p.getCompetition().getSolde()) {
				total += p.getQuantite();
			}
		}
		return total;
	}

}
