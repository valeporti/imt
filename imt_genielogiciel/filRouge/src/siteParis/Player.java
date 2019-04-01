package siteParis;

import java.util.Collection;
import java.util.LinkedList;
import java.util.UUID;


public class Player extends User {
	
	private String passwordPlayer;
	
	/**
	 * @uml.property  name="jetonsQuantity"
	 */
	private long jetonsQuantity; 

	/**
	 * @uml.property   name="paris"
	 * @uml.associationEnd   multiplicity="(0 -1)" inverse="player:siteParis.Pari"
	 */
	private LinkedList<Pari> paris;

	public Player(String nom, String prenom, String pseudo) {
		this.setNom(nom);
		this.setPrenom(prenom);
		this.setPseudo(pseudo);
		this.passwordPlayer = null;
	}

	/**
	 * @param quantity TODO
	 */
	public void competitionInscription(String competition, int quantity){
	}

		
	/**
	 * Getter of the property <tt>jetonsQuantity</tt>
	 * @return  Returns the jetonsQuantity.
	 * @uml.property  name="jetonsQuantity"
	 */
	public long getJetonsQuantity() {
		return jetonsQuantity;
	}
	
	public long addJetons(long plus) {
		long j = this.getJetonsQuantity();
		this.setJetonsQuantity(j + plus);
		return this.getJetonsQuantity();
	}

	public long takeOutJetons(long minus) {
		long j = this.getJetonsQuantity();
		this.setJetonsQuantity(j - minus);
		return this.getJetonsQuantity();
	}

	/**
	 * Getter of the property <tt>paris</tt>
	 * @return  Returns the paris.
	 * @uml.property  name="paris"
	 */
	public LinkedList<Pari> getParis() {
		return paris;
	}
	
	public String getPassword() {
		return passwordPlayer;
	}
	
	public String setPassword() {
		this.passwordPlayer = UUID.randomUUID().toString();
		return this.passwordPlayer;
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
	public void setParis(LinkedList<Pari> paris) {
		this.paris = paris;
	}

}
