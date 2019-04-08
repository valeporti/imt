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

	private String passwordPlayer;

	public Player(String nom, String prenom, String pseudo) {
		this.setNom(nom);
		this.setPrenom(prenom);
		this.setPseudo(pseudo);
		this.passwordPlayer = null;
		this.setParis();
	}

	public long addJetons(long plus) {
		long j = this.getJetonsQuantity();
		this.setJetonsQuantity(j + plus);
		return this.getJetonsQuantity();
	}

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
	
	public void addPari(Pari p) {
		this.paris.add(p);
	}

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

	public String setPassword() {
		this.passwordPlayer = UUID.randomUUID().toString();
		return this.passwordPlayer;
	}

	public long takeOutJetons(long minus) {
		long j = this.getJetonsQuantity();
		this.setJetonsQuantity(j - minus);
		return this.getJetonsQuantity();
	}
	
	public LinkedList<String> getLinkedListPlayer() {
		LinkedList<String> joueur = new LinkedList<String>();
		joueur.add(getNom());
		joueur.add(getPrenom());
		joueur.add(getPseudo());
		joueur.add(Long.toString(getJetonsQuantity()));
		joueur.add(Long.toString(getJetonsInParis()));
		return joueur;
	}
	
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
