package siteParis;

import java.util.Collection;
import java.util.LinkedList;
import java.util.UUID;


public class Player extends User {
	
	/**
	 * Contient la quantité de jetons que le joueur a.
	 */
	private long jetonsQuantity;
	
	/**
	 * Contient les paris auxquels le joueur a fait des paris
	 */
	private LinkedList<Pari> paris; 

	/**
	 * @uml.property  name="passwordPlayer"
	 */
	private String passwordPlayer = null;

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
			if (!p.getCompetition().getSolde()) { // n'a pas été soldé 
				return true;
			}
		}
		return false;
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
	 * Enlever des jetons au joueur
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
	
	// ---- Getters ----
		
	public long getJetonsQuantity() { return jetonsQuantity; }

	public LinkedList<Pari> getParis() { return paris; }
	
	public String getPassword() { return passwordPlayer; }
	
	// ---- Setters ----
	
	public void setJetonsQuantity(long jetonsQuantity) { this.jetonsQuantity = jetonsQuantity; }

	public void setParis() { this.paris = new LinkedList<Pari>(); }

	public String setPassword() {
		this.passwordPlayer = UUID.randomUUID().toString();
		return this.passwordPlayer;
	}

}
