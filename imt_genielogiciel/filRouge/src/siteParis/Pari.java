package siteParis;


public class Pari {

	/**
	 * Contient la compétition liée au pari instancié
	 */
	private Competition competition;

	/**
	 * Contient le joueur lié au pari instancié
	 */
	private Player player;

	/**
	 * Contient la quantité pariée
	 */
	private long quantite;

	/**
	 * Contient le nom du vainqueur envisagé par le joueur
	 */
	private String vainqueur;
	
	/**
	 * Contient la quantité à solder pour le pari instancié, par défaut, initialisé à 0
	 */
	private long a_solder = 0;
	
	/**
	 * constructeur de <code>Pari</code>. 
	 * 
	 * @param vainqueur Nom du copétiteur auquel on veut parier.   
	 * @param quantite quantité de jetons apliqués . 
	 * @param player joueur qui fait le pari. 
	 * @param competition compétition auquelle le joueur pari. 
	 *  
	 */
	public Pari (String vainqueur, long quantite, Player player, Competition competition) {
		this.setCompetition(competition);
		this.setPlayer(player);
		this.setQuantite(quantite);
		this.setVainqueur(vainqueur);
	}
	
	/**
	 * Assigner au joueur la quantité calculé à lui solder lors de la repartition et reinitialiser la valeur
	 *  
	 */
	protected void solder() {
		this.player.addJetons(this.getASolder());
		this.setASolder(0);
	}

	// ---- Getters -----
	
	public Competition getCompetition() { return competition; }

	public Player getPlayer() { return player; }
	
	public long getASolder() { return a_solder; }

	public long getQuantite() { return quantite; }

	public String getVainqueur() { return vainqueur; }
	
	// ---- Setters -----
	
	public void setASolder(long quantite) { this.a_solder = quantite; }

	public void setCompetition(Competition competition) { this.competition = competition; }

	public void setPlayer(Player player) { this.player = player; }

	public void setQuantite(long quantite) { this.quantite = quantite; }

	public void setVainqueur(String vainqueur) { this.vainqueur = vainqueur; }
	
}
