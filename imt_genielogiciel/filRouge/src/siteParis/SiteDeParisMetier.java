package siteParis;


import java.util.LinkedList;
import java.util.Collection;

/**
 * 
 * @author Bernard Prou et Julien Mallet
 * <br><br>
 * La classe qui contient toutes les méthodes "Métier" de la gestion du site de paris. 
 * <br><br>
 * Dans toutes les méthodes :
 * <ul>
 * <li>un paramètre de type <code>String</code> est invalide si il n'est pas instancié.</li>
 *  <li>pour la validité d'un password de gestionnaire et d'un password de joueur :
 * <ul>
 * <li>       lettres et chiffres sont les seuls caractères autorisés </li>
 * <li>       il doit avoir une longueur d'au moins 8 caractères </li>
 * </ul></li>       
 * <li>pour la validité d'un pseudo de joueur  :
 * <ul>
 * <li>        lettres et chiffres sont les seuls caractères autorisés  </li>
 * <li>       il doit avoir une longueur d'au moins 4 caractères</li>
 * </ul></li>       
 * <li>pour la validité d'un prénom de joueur et d'un nom de joueur :
 *  <ul>
 *  <li>       lettres et tiret sont les seuls caractères autorisés  </li>
 *  <li>      il  doit avoir une longueur d'au moins 1 caractère </li>
 * </ul></li>
 * <li>pour la validité d'une compétition  :       
 *  <ul>
 *  <li>       lettres, chiffres, point, trait d'union et souligné sont les seuls caractères autorisés </li>
 *  <li>      elle  doit avoir une longueur d'au moins 4 caractères</li>
 * </ul></li>       
 * <li>pour la validité d'un compétiteur  :       
 *  <ul>
 *  <li>       lettres, chiffres, trait d'union et souligné sont les seuls caractères autorisés </li>
 *  <li>      il doit avoir une longueur d'au moins 4 caractères.</li>
 * </ul></li></ul>
 */

public class SiteDeParisMetier {



	/**
	 * @uml.property  name="competition"
	 * @uml.associationEnd  multiplicity="(0 -1)" inverse="siteDeParisMetier:siteParis.Competition"
	 */
	private LinkedList<Competition> competitions;
	
	private String passwordGestionnaire;
	
	private LinkedList<Player> players;

	/**
	 * constructeur de <code>SiteDeParisMetier</code>. 
	 * 
	 * @param passwordGestionnaire   le password du gestionnaire.   
	 * 
	 * @throws MetierException  levée 
	 * si le <code>passwordGestionnaire</code>  est invalide 
	 */
	public SiteDeParisMetier(String passwordGestionnaire) throws MetierException {
		this.validitePasswordGestionnaire(passwordGestionnaire);
		this.setPassword(passwordGestionnaire);
		this.setPlayers();
		this.setCompetitions();
	}


	// Les méthodes du gestionnaire (avec mot de passe gestionnaire)



	public void addCompetition(Competition competition) {
		this.competitions.add(competition);
	}

	public void addPlayer(Player player) {
		this.players.add(player);
	}



	/**
	 * ajouter une compétition.  
	 * 
	 * @param competition le nom de la compétition
	 * @param dateCloture   la date à partir de laquelle il ne sera plus possible de miser  
	 * @param competiteurs   les noms des différents compétiteurs de la compétition 
	 * @param passwordGestionnaire  le password du gestionnaire du site 
	 * 
	 * @throws MetierException levée si le tableau des
	 * compétiteurs n'est pas instancié, si le
	 * <code>passwordGestionnaire</code> est invalide, si le
	 * <code>passwordGestionnaire</code> est incorrect.
	 * @throws CompetitionExistanteException levée si une compétition existe avec le même nom. 
	 * @throws CompetitionException levée si le nom de la
	 * compétition ou des compétiteurs sont invalides, si il y a
	 * moins de 2 compétiteurs, si un des competiteurs n'est pas instancié,
	 * si deux compétiteurs ont le même nom, si la date de clôture 
	 * n'est pas instanciée ou est dépassée.
	 */
	public void ajouterCompetition(String competition, DateFrancaise dateCloture, String [] competiteurs, String passwordGestionnaire) throws MetierException, CompetitionExistanteException, CompetitionException  {

		if (competition == null || dateCloture == null) throw new CompetitionException();
		this.validitePasswordGestionnaire(passwordGestionnaire);
		if (!this.equalpassword(passwordGestionnaire)) throw new MetierException();
		if (competiteurs == null) throw new MetierException();
		this.validateCompetitionName(competition);
		// la compétition doit avoir plus de 1 competiteur
		if (competiteurs.length < 2) throw new CompetitionException();
		this.validateCompetiteurNom(competiteurs);
		this.validateCompetiteurRepete(competiteurs);
		if (dateCloture.estDansLePasse()) throw new CompetitionException();
		if (this.existingCompetition(competition)) throw new CompetitionExistanteException();
		
		Competition c = new Competition(competition, dateCloture, competiteurs);
		this.addCompetition(c);
	}


	/**
	 * connaître  la liste des noms des compétiteurs d'une compétition.  
	 * 
	 * @param competition   le nom de la compétition  
	 * 
	 * @throws CompetitionException   levée  
	 * si le nom de la compétition est invalide.
	 * @throws CompetitionInexistanteException   levée si il n'existe pas de compétition de même nom. 
	 * 
	 * @return la liste des compétiteurs de la  compétition.
	 */
	public LinkedList <String> consulterCompetiteurs(String competition) throws CompetitionException, CompetitionInexistanteException{
		
		if (competition == null) throw new CompetitionException();
		this.validateCompetitionName(competition);
		if (!this.existingCompetition(competition)) throw new CompetitionInexistanteException();		
		
		return this.getCompetition(competition).getCompetitors();
	}



	/**
	 * connaître les compétitions en cours.
	 * 
	 * @return une liste de liste dont les éléments (de type <code>String</code>) représentent une compétition avec dans l'ordre : 
	 *  <ul>
	 *  <li>       le nom de la compétition,  </li>
	 *  <li>       la date de clôture de la compétition. </li>
	 *  </ul>
	 */
	public LinkedList <LinkedList <String>> consulterCompetitions(){
		
		LinkedList <LinkedList <String>> all_competitions = new LinkedList <LinkedList <String>>();
		for (Competition c: this.getCompetitions()) {
			if (!c.getSolde()) 
				all_competitions.add(c.getLinkedListCompetition());
		}
		return all_competitions;
	}


	/** 
	 * consulter les  joueurs.
	 * 
	 * @param passwordGestionnaire  le password du gestionnaire du site de paris 

	 * @throws MetierException   levée  
	 * si le <code>passwordGestionnaire</code>  est invalide,
	 * si le <code>passwordGestionnaire</code> est incorrect.
	 * 
	 * @return une liste de liste dont les éléments (de type <code>String</code>) représentent un joueur avec dans l'ordre : 
	 *  <ul>
	 *  <li>       le nom du joueur  </li>
	 *  <li>       le prénom du joueur </li>
	 *  <li>       le pseudo du joueur  </li>
	 *  <li>       son compte en jetons restant disponibles </li>
	 *  <li>       le total de jetons engagés dans ses mises en cours. </li>
	 *  </ul>
	 */
	public LinkedList <LinkedList <String>> consulterJoueurs(String passwordGestionnaire) throws MetierException {
		
		this.validitePasswordGestionnaire(passwordGestionnaire);
		LinkedList <LinkedList <String>> all_players = new LinkedList <LinkedList <String>>();
		for (Player p: players) {
			all_players.add(p.getLinkedListPlayer());
		}
		
		return all_players;
	}



	/**
	 * créditer le compte en jetons d'un joueur du site de paris.
	 * 
	 * @param nom   le nom du joueur 
	 * @param prenom   le prénom du joueur   
	 * @param pseudo   le pseudo du joueur  
	 * @param sommeEnJetons   la somme en jetons à créditer  
	 * @param passwordGestionnaire  le password du gestionnaire du site  
	 * 
	 * @throws MetierException   levée 
	 * si le <code>passwordGestionnaire</code>  est invalide,
	 * si le <code>passwordGestionnaire</code> est incorrect,
	 * si la somme en jetons est négative.
	 * @throws JoueurException levée  
	 * si <code>nom</code>, <code>prenom</code>,  <code>pseudo</code> sont invalides.
	 * @throws JoueurInexistantException   levée si il n'y a pas de joueur  avec les mêmes nom,  prénom et pseudo.
	 */
	public void crediterJoueur(String nom, String prenom, String pseudo, long sommeEnJetons, String passwordGestionnaire) throws MetierException, JoueurException, JoueurInexistantException, CrediterException {

		if (nom == null || prenom == null || pseudo == null) throw new JoueurException();
		this.validitePasswordGestionnaire(passwordGestionnaire);
		if (!this.equalpassword(passwordGestionnaire)) throw new MetierException();
		if (!this.existingPlayer(nom, prenom, pseudo)) throw new JoueurInexistantException();
		if (sommeEnJetons <= 0) throw new JoueurException();
		
		Player joueur = getExistingPlayer(nom, prenom, pseudo);
		
		joueur.addJetons(sommeEnJetons);
		
	}








	// Les méthodes avec mot de passe utilisateur


	/**
	 * débiter le compte en jetons d'un joueur du site de paris.
	 * 
	 * @param nom   le nom du joueur 
	 * @param prenom   le prénom du joueur   
	 * @param pseudo   le pseudo du joueur  
	 * @param sommeEnJetons   la somme en jetons à débiter  
	 * @param passwordGestionnaire  le password du gestionnaire du site  
	 * 
	 * @throws MetierException   levée 
	 * si le <code>passwordGestionnaire</code>  est invalide,
	 * si le <code>passwordGestionnaire</code> est incorrect,
	 * si la somme en jetons est négative.
	 * @throws JoueurException levée  
	 * si <code>nom</code>, <code>prenom</code>,  <code>pseudo</code> sont invalides 
	 * si le compte en jetons du joueur est insuffisant (il deviendrait négatif).
	 * @throws JoueurInexistantException   levée si il n'y a pas de joueur  avec les mêmes nom,  prénom et pseudo.
	 * 
	 */

	public void debiterJoueur(String nom, String prenom, String pseudo, long sommeEnJetons, String passwordGestionnaire) throws  MetierException, JoueurInexistantException, JoueurException, DebiterException {

		if (nom == null || prenom == null || pseudo == null) throw new JoueurException();
		this.validitePasswordGestionnaire(passwordGestionnaire);
		if (!this.equalpassword(passwordGestionnaire)) throw new MetierException();
		if (!this.existingPlayer(nom, prenom, pseudo)) throw new JoueurInexistantException();
		if (sommeEnJetons <= 0) throw new JoueurException();
		
		Player joueur = getExistingPlayer(nom, prenom, pseudo);
		
		if (joueur.getJetonsQuantity() < sommeEnJetons) throw new JoueurException();
		
		joueur.takeOutJetons(sommeEnJetons);
		
	}


    

	// Les méthodes sans mot de passe


	/**
	 * supprimer un joueur. 
	 * 
	 * @param nom   le nom du joueur 
	 * @param prenom   le prénom du joueur   
	 * @param pseudo   le pseudo du joueur  
	 * @param passwordGestionnaire  le password du gestionnaire du site  
	 * 
	 * @throws MetierException
	 * si le <code>passwordGestionnaire</code>  est invalide,
	 * si le <code>passwordGestionnaire</code> est incorrect.
	 * @throws JoueurInexistantException   levée si il n'y a pas de joueur  avec le même <code>nom</code>, <code>prenom</code>  et <code>pseudo</code>.
	 * @throws JoueurException levée 
	 * si le joueur a des paris en cours,
	 * si <code>nom</code>, <code>prenom</code>, <code>pseudo</code> sont invalides.
	 * 
	 * @return le nombre de jetons à rembourser  au joueur qui vient d'être désinscrit.
	 * 
	 */
	public long desinscrireJoueur(String nom, String prenom, String pseudo, String passwordGestionnaire) throws MetierException, JoueurInexistantException, JoueurException {
		
		if (nom == null || prenom == null || pseudo == null) throw new JoueurException();
		this.validitePasswordGestionnaire(passwordGestionnaire);
		if (!this.existingPlayer(nom, prenom, pseudo)) throw new JoueurInexistantException();
		
		Player p = this.getPlayer(nom, prenom, pseudo);
		long jetons =  p.getJetonsQuantity();
		players.remove(p);
		return jetons;
		
	} 

	protected boolean equalpassword(String p) { return p.equals(this.passwordGestionnaire); }
	
	public boolean existingCompetition (String competition) {
		for (Competition c: competitions) {
			//System.out.println("checking: " + c.getNom() + " == " +  competition );
			if (competition.equals(c.getNom())) {
				return true;
			}
		}
		return false;
	}
	
	
	public boolean existingPlayer (String pseudo, String pass) {
		for (Player p: players) {
			if (pseudo.equals(p.getPseudo()) && pass.equals(p.getPassword())) {
				return true;
			}
		}
		return false;
	}
	
	public boolean existingPlayer (String nom, String prenom, String pseudo) {
		for (Player p: players) {
			if (nom.equals(p.getNom()) && prenom.equals(p.getPrenom()) || pseudo.equals(p.getPseudo())) {
				return true;
			}
		}
		return false;
	}
	
	public Competition getCompetition(String competition) {
		for (Competition c: competitions) {
			//System.out.println("checking: " + c.getNom() + " == " +  competition );
			if (competition.equals(c.getNom())) {
				return c;
			}
		}
		return null;
	}
	
	/**
	 * Getter of the property <tt>competition</tt>
	 * @return  Returns the competition.
	 * @uml.property  name="competition"
	 */
	public LinkedList<Competition> getCompetitions() {
		return competitions;
	}
	
	public Player getExistingPlayer (String nom, String prenom, String pseudo) {
		for (Player p: players) {
			if (nom.equals(p.getNom()) && prenom.equals(p.getPrenom()) || pseudo.equals(p.getPseudo())) {
				return p;
			}
		}
		return null;
	}
	

	public Player getPlayer(String pseudo, String password) {
		for (Player p: players) {
			if (pseudo.equals(p.getPseudo()) && password.equals(p.getPassword())) {
				return p;
			}
		}
		return null;
	}
	
	public Player getPlayer(String nom, String prenom, String pseudo) {
		for (Player p: players) {
			if (nom.equals(p.getNom()) && prenom.equals(p.getPrenom()) || pseudo.equals(p.getPseudo())) {
				return p;
			}
		}
		return null;
	}
	
	/**
	 * inscrire un joueur. 
	 * 
	 * @param nom   le nom du joueur 
	 * @param prenom   le prénom du joueur   
	 * @param pseudo   le pseudo du joueur  
	 * @param passwordGestionnaire  le password du gestionnaire du site  
	 * 
	 * @throws MetierException   levée  
	 * si le <code>passwordGestionnaire</code> proposé est invalide,
	 * si le <code>passwordGestionnaire</code> est incorrect.
	 * @throws JoueurExistantException   levée si un joueur existe avec les mêmes noms et prénoms ou le même pseudo.
	 * @throws JoueurException levée si <code>nom</code>, <code>prenom</code>, <code>pseudo</code> sont invalides.
	 * 
	 * @return le mot de passe (déterminé par le site) du nouveau joueur inscrit.
	 */
	public String inscrireJoueur(String nom, String prenom, String pseudo, String passwordGestionnaire) throws MetierException, JoueurExistantException, JoueurException {
		
		
		if (nom == null || prenom == null || pseudo == null) throw new JoueurException();
		this.validitePasswordGestionnaire(passwordGestionnaire);
		if (!this.equalpassword(passwordGestionnaire)) throw new MetierException();
		if (this.existingPlayer(nom, prenom, pseudo)) throw new JoueurExistantException();
		if (!nom.matches("^[a-zA-Z]+$") || !prenom.matches("^[a-zA-Z]+$")) throw new JoueurException();
		if (!pseudo.matches("^[a-zA-Z]{4,}$")) throw new JoueurException();
		
		
		Player joueur = new Player(nom, prenom, pseudo);
		addPlayer(joueur);
		String new_password = joueur.setPassword();
		
		return new_password;
	}

	public boolean isEmptyPlayers() { return players.size() == 0; }
	
	/**
	 * miserVainqueur  (parier sur une compétition, en désignant un vainqueur).
	 * Le compte du joueur est débité du nombre de jetons misés.
	 * 
	 * @param pseudo   le pseudo du joueur  
	 * @param passwordJoueur  le password du joueur  
	 * @param miseEnJetons   la somme en jetons à miser  
	 * @param competition   le nom de la compétition  relative au pari effectué
	 * @param vainqueurEnvisage   le nom du compétiteur  sur lequel le joueur mise comme étant le  vainqueur de la compétition  
	 * 
	 * @throws MetierException levée si la somme en jetons est négative.
	 * @throws JoueurInexistantException levée si il n'y a pas de
	 * joueur avec les mêmes pseudos et password.
	 * @throws CompetitionInexistanteException   levée si il n'existe pas de compétition de même nom. 
	 * @throws CompetitionException levée 
	 * si <code>competition</code> ou <code>vainqueurEnvisage</code> sont invalides,
	 * si il n'existe pas un compétiteur de  nom <code>vainqueurEnvisage</code> dans la compétition,
	 * si la compétition n'est plus ouverte (la date de clôture est dans le passé).
	 * @throws JoueurException   levée 
	 * si <code>pseudo</code> ou <code>password</code> sont invalides, 
	 * si le <code>compteEnJetons</code> du joueur est insuffisant (il deviendrait négatif).
	 */
    public void miserVainqueur(String pseudo, String passwordJoueur, long miseEnJetons, String competition, String vainqueurEnvisage) throws MetierException, JoueurInexistantException, CompetitionInexistanteException, CompetitionException, JoueurException  {

    	if (pseudo == null) throw new JoueurException();
    	if (miseEnJetons < 0) throw new MetierException();
    	if (validPlayerAlmost(pseudo, passwordJoueur)) throw new JoueurException();
    	if (!existingPlayer(pseudo, passwordJoueur)) throw new JoueurInexistantException();
    	
    	
    	Player joueur = this.getPlayer(pseudo, passwordJoueur);
    	
    	if (!this.existingCompetition(competition)) throw new CompetitionInexistanteException();
    	
    	Competition comp = this.getCompetition(competition);
    	
    	if (!comp.competiteurExistant(vainqueurEnvisage)) throw new CompetitionException();
    	if (joueur.getJetonsQuantity() - miseEnJetons < 0) throw new JoueurException();
    	
    	Pari pari = new Pari(vainqueurEnvisage, miseEnJetons, joueur, comp);
    	
    	joueur.addPari(pari);
    	joueur.takeOutJetons(miseEnJetons);
    	comp.addPari(pari);
	}
	
	/**
	 * Setter of the property <tt>competition</tt>
	 * @param competition  The competition to set.
	 * @uml.property  name="competition"
	 */
	public void setCompetitions() {
		this.competitions = new LinkedList<Competition>();
	}
	
	public void setPassword(String pass) {
		this.passwordGestionnaire = pass;
	}
	
	public void setPlayers() {
		this.players = new LinkedList<Player>();
	}

	/**
	 * solder une compétition vainqueur (compétition avec vainqueur).  
	 * 
	 * Chaque joueur ayant misé sur cette compétition
	 * en choisissant ce compétiteur est crédité d'un nombre de
	 * jetons égal à :
	 * 
	 * (le montant de sa mise * la somme des
	 * jetons misés pour cette compétition) / la somme des jetons
	 * misés sur ce compétiteur.
	 *
	 * Si aucun joueur n'a trouvé le
	 * bon compétiteur, des jetons sont crédités aux joueurs ayant
	 * misé sur cette compétition (conformément au montant de
	 * leurs mises). La compétition est "supprimée" si il ne reste
	 * plus de mises suite à ce solde.
	 * 
	 * @param competition   le nom de la compétition  
	 * @param vainqueur   le nom du vainqueur de la compétition 
	 * @param passwordGestionnaire  le password du gestionnaire du site 
	 * 
	 * @throws MetierException   levée 
	 * si le <code>passwordGestionnaire</code>  est invalide,
	 * si le <code>passwordGestionnaire</code> est incorrect.
	 * @throws CompetitionInexistanteException   levée si il n'existe pas de compétition de même nom.
	 * @throws CompetitionException levée 
	 * si le nom de la compétition ou du vainqueur est invalide, 
	 * si il n'existe pas de compétiteur du nom du vainqueur dans la compétition,
	 * si la date de clôture de la compétition est dans le futur.
	 * 
	 */	
	public void solderVainqueur(String competition, String vainqueur, String passwordGestionnaire) throws MetierException, CompetitionInexistanteException, CompetitionException  {
		
		this.validitePasswordGestionnaire(passwordGestionnaire);
		if (!this.existingCompetition(competition)) throw new CompetitionInexistanteException();
	
		Competition comp = this.getCompetition(competition);
		
		if (!comp.competiteurExistant(vainqueur)) throw new CompetitionException();
		if (!comp.getDate().estDansLePasse()) throw new CompetitionException();
		if (comp.getSolde()) throw new CompetitionInexistanteException();
		
		LinkedList<Pari> paris_vainqueurs = comp.getParisVainqueurs(vainqueur);
		this.calculerMontantParPari(paris_vainqueurs, comp.getParis());
		this.distribuerASolder(paris_vainqueurs);
		comp.setSolde(true);
		
	}
	
	protected void distribuerASolder(LinkedList<Pari> paris_vainqueurs) {
		for (Pari pari: paris_vainqueurs) {
			pari.solder();
		}
	}
	
	protected long calculerMontantTotal(LinkedList<Pari> paris) {
		long somme_totale = 0;
		for (Pari pari: paris) {
			somme_totale += pari.getQuantite();
		}
		return somme_totale;
	}
	
	protected void calculerMontantParPari(LinkedList<Pari> paris_vainqueurs, LinkedList<Pari> paris) {
		long somme_totale = this.calculerMontantTotal(paris);
		long somme_sur_ce_competiteur = this.calculerMontantTotal(paris_vainqueurs);
		for (Pari pari: paris_vainqueurs) {

			// montant de sa mise * la somme des jetons misés pour cette compétition) / la somme des jetons
			// misés sur ce compétiteur
			long sa_mise = pari.getQuantite();
			long total = sa_mise * somme_totale / somme_sur_ce_competiteur;
			pari.setASolder(total);
		}
	}


	protected void validateCompetiteurNom(String [] noms) throws CompetitionException {
		for (String n : noms) {
			if (n == null || n.length() < 4 || !n.matches("^[a-zA-Z]+$")) throw new CompetitionException();
		}	
	}

	protected void validateCompetiteurRepete(String [] noms) throws CompetitionException {
		for (String n : noms) {
			int count = 0;
			for (String nom : noms) {
				//System.out.println("checking: " + n + " == " +  nom );
				if (n.equals(nom)) ++ count ;
				//System.out.println("checking: " + count );
				if (count > 1) throw new CompetitionException();
			}
		}	
	}
	
	protected void validateCompetitionName(String competition) throws CompetitionException {
		//System.out.println("checking: " + competition);
		if (competition == null) throw new CompetitionException();
		if (competition.length() < 4) throw new CompetitionException();
		if (!competition.matches("^[a-zA-Z0-9]+$")) throw new CompetitionException();		
	}
	
	/**
	 * vérifier la validité du password du gestionnaire.
	 * 
	 * @param passwordGestionnaire   le password du gestionnaire à vérifier
	 * 
	 * @throws MetierException   levée 
	 * si le <code>passwordGestionnaire</code> est invalide.  
	 */
	protected void validitePasswordGestionnaire(String passwordGestionnaire) throws MetierException {
	    if (passwordGestionnaire==null) throw new MetierException();
	    if (!passwordGestionnaire.matches("[0-9A-Za-z]{8,}")) throw new MetierException();
	    if (this.passwordGestionnaire != null && !this.passwordGestionnaire.equals(passwordGestionnaire)) throw new MetierException();
	}
	
	public boolean validPlayerAlmost (String pseudo, String pass) {
		for (Player p: players) {
			if ((pseudo.equals(p.getPseudo()) && !pass.equals(p.getPassword())) || (!pseudo.equals(p.getPseudo()) && pass.equals(p.getPassword()))) {
				return true;
			}
		}
		return false;
	}
	

}


