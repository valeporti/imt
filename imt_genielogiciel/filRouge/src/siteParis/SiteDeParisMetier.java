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
	 * Contient toutes les compétitions enregistrées
	 */
	private LinkedList<Competition> competitions;
	
	/**
	 * Contient le mot de passe du gestionnaire de l'instance créé du SiteParisMetier
	 */
	private String passwordGestionnaire;
	
	/**
	 * Contient tous les joureurs enregistrés
	 */
	private LinkedList<Player> players;

	/**
	 * constructeur de <code>SiteDeParisMetier</code>. 
	 * 
	 * @param passwordGestionnaire le password du gestionnaire.   
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

	/**
	 * Ajouter une compétition à la liste
	 * 
	 * @param competition
	 *  
	 */
	public void addCompetition(Competition competition) {
		this.competitions.add(competition);
	}

	/**
	 * Ajouter un joueur à la liste
	 * 
	 * @param player
	 *  
	 */
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

		this.validateCompetitionInputs(competition, dateCloture, competiteurs);
		this.validitePasswordGestionnaire(passwordGestionnaire);
		if (!this.equalpassword(passwordGestionnaire)) throw new MetierException();

		Competition c = new Competition(competition, dateCloture, competiteurs);
		this.addCompetition(c);
	}
	
	/**
	 * 
	 * Valide et évalue la nature de l'information pour la compétition
	 * 
	 * @param competition
	 * @param dateCloture
	 * @param competiteurs
	 * @throws CompetitionException
	 * @throws MetierException
	 * @throws CompetitionExistanteException
	 */
	public void validateCompetitionInputs(String competition, DateFrancaise dateCloture, String [] competiteurs) throws CompetitionException, MetierException, CompetitionExistanteException {
		if (competition == null || dateCloture == null) throw new CompetitionException();
		if (competiteurs == null) throw new MetierException();
		this.validateCompetitionName(competition);
		// la compétition doit avoir plus de 1 competiteur
		if (competiteurs.length < 2) throw new CompetitionException();
		this.validateCompetiteurNom(competiteurs);
		this.validateCompetiteurRepete(competiteurs);
		if (dateCloture.estDansLePasse()) throw new CompetitionException();
		if (this.existingCompetition(competition)) throw new CompetitionExistanteException();
	}


	/**
	 * calculer le montant total a solder par pari.
	 * en cas de non vainqueur choisi, le montant est redistribué à ceux ayant fait un pari 
	 * 
	 * @param paris le total des paris à traiter
	 * @param paris_vainqueurs les paris des vainqueurs si existants
	 */
	protected void calculerMontantParPari(LinkedList<Pari> paris_vainqueurs, LinkedList<Pari> paris) {
		long somme_totale = this.calculerMontantTotal(paris);
		long somme_sur_ce_competiteur = this.calculerMontantTotal(paris_vainqueurs);
		
		if (paris_vainqueurs.isEmpty()) {
			for (Pari pari: paris) {
				// retourner
				pari.setASolder(pari.getQuantite());
			}
		} else {
			for (Pari pari: paris_vainqueurs) {
				// montant de sa mise * la somme des jetons misés pour cette compétition) / la somme des jetons
				// misés sur ce compétiteur
				long sa_mise = pari.getQuantite();
				long total = sa_mise * somme_totale / somme_sur_ce_competiteur;
				pari.setASolder(total);
			}
		}
	}



	/**
	 * calculer le montant total parié dans un ensemble de paris donné.
	 * 
	 * @param paris les paris 
	 *  
	 */
	protected long calculerMontantTotal(LinkedList<Pari> paris) {
		long somme_totale = 0;
		for (Pari pari: paris) {
			somme_totale += pari.getQuantite();
		}
		return somme_totale;
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


	// Les méthodes avec mot de passe utilisateur


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
		for (Player p: this.getPlayers()) {
			all_players.add(p.getLinkedListPlayer());
		}
		
		return all_players;
	}


    

	// Les méthodes sans mot de passe


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

		this.validatePlayerInfo(nom, prenom, pseudo);
		this.validitePasswordGestionnaire(passwordGestionnaire);
		if (!this.equalpassword(passwordGestionnaire)) throw new MetierException();
		if (!this.existingPlayer(nom, prenom, pseudo)) throw new JoueurInexistantException();
		if (sommeEnJetons <= 0) throw new MetierException();
		
		Player joueur = getExistingPlayer(nom, prenom, pseudo);
		
		joueur.addJetons(sommeEnJetons);
		
	} 

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
		
		this.validatePlayerInfo(nom, prenom, pseudo);
		this.validitePasswordGestionnaire(passwordGestionnaire);
		
		if (!this.equalpassword(passwordGestionnaire)) throw new MetierException();
		if (!this.existingPlayer(nom, prenom, pseudo)) throw new JoueurInexistantException();
		if (sommeEnJetons <= 0) throw new MetierException();
		
		Player joueur = getExistingPlayer(nom, prenom, pseudo);
		
		if (joueur.getJetonsQuantity() < sommeEnJetons) throw new JoueurException();
		
		joueur.takeOutJetons(sommeEnJetons);
		
	}
	
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
		
		this.validatePlayerInfo(nom, prenom, pseudo);
		this.validitePasswordGestionnaire(passwordGestionnaire);
		if (!this.existingNomPrenomOuPseudo(nom, prenom, pseudo)) throw new JoueurInexistantException();
		
		Player joueur = this.getPlayer(nom, prenom, pseudo);
		
		if (joueur.parisEnCours()) throw new JoueurException();
		
		long jetons = joueur.getJetonsQuantity();
		players.remove(joueur);
		return jetons;
		
	}
	
	/**
	 * distribuer la quantité due à chaque competiteur.
	 * 
	 * @param paris_vainqueurs les paris qui ont choisi un vainqueur
	 *  
	 */
	protected void distribuerASolder(LinkedList<Pari> paris_vainqueurs) {
		for (Pari pari: paris_vainqueurs) {
			pari.solder();
		}
	}
	
	/**
	 * Verifier l'égalité d'un password introduit
	 * 
	 * @param p password gestionnaire
	 *  
	 */
	protected boolean equalpassword(String p) { return p.equals(this.passwordGestionnaire); }
	
	/**
	 * Verifier existance d'une compétition
	 * 
	 * @param competition nom competition
	 *  
	 */
	public boolean existingCompetition (String competition) {
		for (Competition c: this.getCompetitions()) {
			if (competition.equals(c.getNom())) {
				return true;
			}
		}
		return false;
	}
	
	/**
	 * Verifier si'il y un un joueur avec le pseudo et le password indiquées
	 * 
	 * @param pseudo joueur
	 * @param pass joueur
	 *  
	 */
	public boolean existingPlayerPseudoPass (String pseudo, String pass) {
		for (Player p: this.getPlayers()) {
			if (pseudo.equals(p.getPseudo()) && pass.equals(p.getPassword())) {
				return true;
			}
		}
		return false;
	}
	
	/**
	 * Verifier si'il y un un joueur avec les caractéristiques introduites
	 * 
	 * @param nom joueur
	 * @param prenom joueur
	 * @param pseudo joueur
	 *  
	 */
	public boolean existingPlayer (String nom, String prenom, String pseudo) {
		for (Player p: this.getPlayers()) {
			if (nom.equals(p.getNom()) && prenom.equals(p.getPrenom()) && pseudo.equals(p.getPseudo())) {
				return true;
			}
		}
		return false;
	}
	
	/**
	 * Verifier si'il y un un joueur avec soit le nom et prenom ou le pseudo déjà existant
	 * 
	 * @param nom joueur
	 * @param prenom joueur
	 * @param pseudo joueur
	 *  
	 */
	public boolean existingNomPrenomOuPseudo(String nom, String prenom, String pseudo) {
		for (Player p: this.getPlayers()) {
			if (nom.equals(p.getNom()) && prenom.equals(p.getPrenom()) || pseudo.equals(p.getPseudo())) {
				return true;
			}
		}
		return false;
	}
	

	/**
	 * Retourner la competition à partir de son nom
	 * 
	 * @param competition nom competition
	 *  
	 */
	public Competition getCompetition(String competition) {
		for (Competition c: this.getCompetitions()) {
			if (competition.equals(c.getNom())) {
				return c;
			}
		}
		return null;
	}
	
	/**
	 * Vérifie si jamais le joueur (nom, prenom, pseudo) existe déjà
	 * 
	 * @param competition nom competition
	 * @param competition prenom competition
	 * @param competition pseudo competition
	 *  
	 */
	public Player getExistingPlayer (String nom, String prenom, String pseudo) {
		for (Player p: this.getPlayers()) {
			if (nom.equals(p.getNom()) && prenom.equals(p.getPrenom()) && pseudo.equals(p.getPseudo())) {
				return p;
			}
		}
		return null;
	}

	/**
	 * Retourne la coincidence d'un joueur à partir des paramètres pseudo et password
	 * 
	 * @param String pseudo
	 * @param String password
	 */
	public Player getPlayer(String pseudo, String password) {
		for (Player p: this.getPlayers()) {
			if (pseudo.equals(p.getPseudo()) && password.equals(p.getPassword())) {
				return p;
			}
		}
		return null;
	}
	
	/**
	 * Retourne la coincidence d'un joueur à partir des paramètres pseudo, nom et prénom
	 * 
	 * @param String pseudo
	 * @param String prenom
	 * @param String nom
	 */
	public Player getPlayer(String nom, String prenom, String pseudo) {
		for (Player p: this.getPlayers()) {
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
		
		this.validitePasswordGestionnaire(passwordGestionnaire);
		this.validatePlayerInfo(nom, prenom, pseudo);
		if (!this.equalpassword(passwordGestionnaire)) throw new MetierException();
		if (this.existingNomPrenomOuPseudo(nom, prenom, pseudo)) throw new JoueurExistantException();
		
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

    	this.validatePlayerPassPseudo(passwordJoueur, pseudo);
    	if (validPlayerAlmost(pseudo, passwordJoueur)) throw new JoueurException();
    	if (!existingPlayerPseudoPass(pseudo, passwordJoueur)) throw new JoueurInexistantException();
    	
    	Player joueur = this.getPlayer(pseudo, passwordJoueur);
    	
    	this.validateCompetitionName(competition);
    	this.validateCompetiteurNom(new String[] {vainqueurEnvisage});
    	if (!this.existingCompetition(competition)) throw new CompetitionInexistanteException();
    	
    	Competition comp = this.getCompetition(competition);

    	if (miseEnJetons < 0) throw new MetierException();
    	if (!comp.competiteurExistant(vainqueurEnvisage)) throw new CompetitionException();
    	if (joueur.getJetonsQuantity() - miseEnJetons < 0) throw new JoueurException();
    	//System.out.println(comp.getDate().estDansLePasse());
    	if (comp.getDate().estDansLePasse() || comp.getSolde()) throw new CompetitionException();
    	
    	Pari pari = new Pari(vainqueurEnvisage, miseEnJetons, joueur, comp);
    	
    	joueur.addPari(pari);
    	joueur.takeOutJetons(miseEnJetons);
    	comp.addPari(pari);
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
		this.validateCompetitionName(competition);
		this.validateCompetiteurNom(new String[] {vainqueur});
	
		Competition comp = this.getCompetition(competition);
		
		if (!comp.competiteurExistant(vainqueur)) throw new CompetitionException();
		if (!comp.getDate().estDansLePasse()) throw new CompetitionException();
		if (comp.getSolde()) throw new CompetitionInexistanteException();
		
		LinkedList<Pari> paris_vainqueurs = comp.getParisVainqueurs(vainqueur);
		this.calculerMontantParPari(paris_vainqueurs, comp.getParis());
		if (paris_vainqueurs.isEmpty()) { // retourner les jetons
			this.distribuerASolder(comp.getParis());
		} else {
			this.distribuerASolder(paris_vainqueurs);
		}
		comp.setSolde(true);
		
	}


	/**
	 * Verifier la validité du nom des competiteurs
	 * 
	 * @param noms les noms à verifier
	 *  
	 */
	protected void validateCompetiteurNom(String [] noms) throws CompetitionException {
		for (String n : noms) {
			if (n == null || n.length() < 4 || !n.matches("^[a-zA-Z]+$")) throw new CompetitionException();
		}	
	}

	/**
	 * Verifier si jamais il y a un competiteur qui se repète dans la liste noms
	 * 
	 * @param noms les noms à verifier
	 *  
	 */
	protected void validateCompetiteurRepete(String [] noms) throws CompetitionException {
		for (String n : noms) {
			int count = 0;
			for (String nom : noms) {
				if (n.equals(nom)) ++ count ;
				if (count > 1) throw new CompetitionException();
			}
		}	
	}
	
	/**
	 * Valider le nom de la compétition
	 * 
	 * @param competition nom competition
	 *  
	 */
	protected void validateCompetitionName(String competition) throws CompetitionException {
		if (competition == null) throw new CompetitionException();
		if (competition.length() < 4) throw new CompetitionException();
		if (!competition.matches("^[a-zA-Z0-9]+$")) throw new CompetitionException();		
	}
	
	/**
	 * Valider l'information du joueur
	 * 
	 * @param nom
	 * @param prenom
	 * @param pseudo
	 * 
	 * @throws JoueurException   levée 
	 * si le <code>nom</code> ou <code>prenom</code> ou <code>pseudo</code> sont invalides. 
	 *  
	 */
	protected void validatePlayerInfo(String nom, String prenom, String pseudo) throws JoueurException {
		if (nom == null || prenom == null || pseudo == null) throw new JoueurException();
		if (!nom.matches("^[a-zA-Z]+$") || !prenom.matches("^[a-zA-Z]+$")) throw new JoueurException();
		if (!pseudo.matches("^[a-zA-Z]{4,}$")) throw new JoueurException();
	}
	
	/**
	 * Valider l'information du joueur, juste pseudo et password
	 * 
	 * @param password
	 * @param pseudo
	 * 
	 * @throws JoueurException   levée 
	 * si le <code>password</code> ou <code>pseudo</code> sont invalides. 
	 *  
	 */
	protected void validatePlayerPassPseudo(String password, String pseudo) throws JoueurException {
		if (password == null || pseudo == null) throw new JoueurException();
		if (!password.matches("^[-a-zA-Z0-9]{4,}$")) throw new JoueurException();
		if (!pseudo.matches("^[a-zA-Z]{4,}$")) throw new JoueurException();
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
	    if (this.getPasswordGestionnaire() != null && !this.getPasswordGestionnaire().equals(passwordGestionnaire)) throw new MetierException();
	}
	
	/**
	 * Valider si on a introduit un joueur à moitié bien, c'est à dire, il y a un coincidence pas complète
	 * 
	 * @param pseudo le pseudo du joueur
	 * @param pass le mot de passe du joueur
	 *  
	 */
	public boolean validPlayerAlmost (String pseudo, String pass) {
		for (Player p: players) {
			if ((pseudo.equals(p.getPseudo()) && !pass.equals(p.getPassword())) || (!pseudo.equals(p.getPseudo()) && pass.equals(p.getPassword()))) {
				return true;
			}
		}
		return false;
	}
	
	// ---- Getters ----
	
	public LinkedList<Competition> getCompetitions() { return competitions; }
	
	public LinkedList<Player> getPlayers() { return players; }
	
	public String getPasswordGestionnaire() { return passwordGestionnaire; }
	
	
	// ---- Setters ----

	public void setCompetitions() { this.competitions = new LinkedList<Competition>(); }
	
	public void setPassword(String pass) { this.passwordGestionnaire = pass; }

	public void setPlayers() { this.players = new LinkedList<Player>(); }

}


