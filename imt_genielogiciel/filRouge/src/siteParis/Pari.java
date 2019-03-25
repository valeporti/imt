package siteParis;


public class Pari {

	/**
	 * @uml.property  name="competition"
	 * @uml.associationEnd  inverse="paris:siteParis.Competition"
	 */
	private Competition competition;

	/**
	 * Getter of the property <tt>competition</tt>
	 * @return  Returns the competition.
	 * @uml.property  name="competition"
	 */
	public Competition getCompetition() {
		return competition;
	}

	/**
	 * Setter of the property <tt>competition</tt>
	 * @param competition  The competition to set.
	 * @uml.property  name="competition"
	 */
	public void setCompetition(Competition competition) {
		this.competition = competition;
	}

	/**
	 * @uml.property  name="player"
	 * @uml.associationEnd  inverse="paris:siteParis.Player"
	 */
	private Player player;

	/**
	 * Getter of the property <tt>player</tt>
	 * @return  Returns the player.
	 * @uml.property  name="player"
	 */
	public Player getPlayer() {
		return player;
	}

	/**
	 * Setter of the property <tt>player</tt>
	 * @param player  The player to set.
	 * @uml.property  name="player"
	 */
	public void setPlayer(Player player) {
		this.player = player;
	}

	/**
	 * @uml.property  name="quantite"
	 */
	private int quantite;

	/**
	 * Getter of the property <tt>quantite</tt>
	 * @return  Returns the quantite.
	 * @uml.property  name="quantite"
	 */
	public int getQuantite() {
		return quantite;
	}

	/**
	 * Setter of the property <tt>quantite</tt>
	 * @param quantite  The quantite to set.
	 * @uml.property  name="quantite"
	 */
	public void setQuantite(int quantite) {
		this.quantite = quantite;
	}

	/**
	 * @uml.property  name="vainqueur"
	 */
	private String vainqueur;

	/**
	 * Getter of the property <tt>vainqueur</tt>
	 * @return  Returns the vainqueur.
	 * @uml.property  name="vainqueur"
	 */
	public String getVainqueur() {
		return vainqueur;
	}

	/**
	 * Setter of the property <tt>vainqueur</tt>
	 * @param vainqueur  The vainqueur to set.
	 * @uml.property  name="vainqueur"
	 */
	public void setVainqueur(String vainqueur) {
		this.vainqueur = vainqueur;
	}

}
