package siteParis;


public class Pari {

	/**
	 * @uml.property  name="competition"
	 * @uml.associationEnd  inverse="paris:siteParis.Competition"
	 */
	private Competition competition;

	/**
	 * @uml.property  name="player"
	 * @uml.associationEnd  inverse="paris:siteParis.Player"
	 */
	private Player player;

	/**
	 * @uml.property  name="quantite"
	 */
	private long quantite;

	/**
	 * @uml.property  name="vainqueur"
	 */
	private String vainqueur;
	
	private long a_solder;
	
	public Pari (String vainqueur, long quantite, Player player, Competition competition) {
		this.setCompetition(competition);
		this.setPlayer(player);
		this.setQuantite(quantite);
		this.setVainqueur(vainqueur);
		this.setASolder(0);
	}

	/**
	 * Getter of the property <tt>competition</tt>
	 * @return  Returns the competition.
	 * @uml.property  name="competition"
	 */
	public Competition getCompetition() {
		return competition;
	}

	/**
	 * Getter of the property <tt>player</tt>
	 * @return  Returns the player.
	 * @uml.property  name="player"
	 */
	public Player getPlayer() {
		return player;
	}
	
	public long getASolder() {
		return a_solder;
	}

	/**
	 * Getter of the property <tt>quantite</tt>
	 * @return  Returns the quantite.
	 * @uml.property  name="quantite"
	 */
	public long getQuantite() {
		return quantite;
	}

	/**
	 * Getter of the property <tt>vainqueur</tt>
	 * @return  Returns the vainqueur.
	 * @uml.property  name="vainqueur"
	 */
	public String getVainqueur() {
		return vainqueur;
	}
	
	public void setASolder(long quantite) {
		this.a_solder = quantite;
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
	 * Setter of the property <tt>player</tt>
	 * @param player  The player to set.
	 * @uml.property  name="player"
	 */
	public void setPlayer(Player player) {
		this.player = player;
	}

	/**
	 * Setter of the property <tt>quantite</tt>
	 * @param quantite  The quantite to set.
	 * @uml.property  name="quantite"
	 */
	public void setQuantite(long quantite) {
		this.quantite = quantite;
	}

	/**
	 * Setter of the property <tt>vainqueur</tt>
	 * @param vainqueur  The vainqueur to set.
	 * @uml.property  name="vainqueur"
	 */
	public void setVainqueur(String vainqueur) {
		this.vainqueur = vainqueur;
	}
	
	protected void solder() {
		this.player.addJetons(this.getASolder());
		this.setASolder(0);
	}

}
