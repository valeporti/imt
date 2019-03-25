package siteParis;

import java.util.Collection;


public class Player extends User {
	
	public Player(String nom, String prenom, String pseudo) {
		this.setNom(nom);
		this.setPrenom(prenom);
		this.setPseudo(pseudo);
	} 

	/**
	 * @uml.property  name="jetonsQuantity"
	 */
	private long jetonsQuantity;

	/**
	 * Getter of the property <tt>jetonsQuantity</tt>
	 * @return  Returns the jetonsQuantity.
	 * @uml.property  name="jetonsQuantity"
	 */
	public long getJetonsQuantity() {
		return jetonsQuantity;
	}

	/**
	 * Setter of the property <tt>jetonsQuantity</tt>
	 * @param jetonsQuantity  The jetonsQuantity to set.
	 * @uml.property  name="jetonsQuantity"
	 */
	public void setJetonsQuantity(int jetonsQuantity) {
		this.jetonsQuantity = jetonsQuantity;
	}

		
	/**
	 * @param quantity TODO
	 */
	public void competitionInscription(String competition, int quantity){
	}


	/**
	 * @uml.property   name="paris"
	 * @uml.associationEnd   multiplicity="(0 -1)" inverse="player:siteParis.Pari"
	 */
	private Collection paris;

	/**
	 * Getter of the property <tt>paris</tt>
	 * @return  Returns the paris.
	 * @uml.property  name="paris"
	 */
	public Collection getParis() {
		return paris;
	}

	/**
	 * Setter of the property <tt>paris</tt>
	 * @param paris  The paris to set.
	 * @uml.property  name="paris"
	 */
	public void setParis(Collection paris) {
		this.paris = paris;
	}

}
