package siteParis;

import java.util.Collection;
import java.util.LinkedList;
import java.util.Arrays;


public class Competition {

	/**
	 * Contient les competiteurs de la compétition
	 */
	private LinkedList<String> competitors;

	/**
	 * Contient la date de la réalisation de la compétition
	 */
	private DateFrancaise date;
	
	/**
	 * Contient le nom de la compétition
	 */
	private String nom;

	/**
	 * Contient la liste des paris associés à l'instance de Compétition
	 */
	private LinkedList<Pari> paris;

	/**
	 * Indique si la repartition des jetons liés à cette compétition ont été déjà repartis
	 */
	private boolean solde = false;
	
	/**
	 * constructeur de <code>Competition</code>. 
	 * 
	 * @param nom Nom de la Compétition.   
	 * @param dateCloture date de cloture. 
	 * @param competiteurs liste de compétiteurs. 
	 *  
	 */
	public Competition (String nom, DateFrancaise dateCloture, String [] competiteurs) {
		this.setNom(nom);
		this.setDate(dateCloture);
		this.paris = new LinkedList<Pari>();
		this.setCompetitors(competiteurs);
	}
	
	/**
	 * Ajouter un pari
	 * 
	 * @param p pari à ajouter
	 * 
	 */
	public void addPari(Pari p) { this.paris.add(p); }  
	
	/**
	 * Vérifie l'existance d'un compétiteur dans la liste des compétiteurs de l'instance Compétition
	 * 
	 * @param competiteur
	 *
	 */
	protected boolean competiteurExistant (String competiteur) {
		for (String c: this.getCompetitors()) {
			if (competiteur.equals(c)) {
				return true;
			}
		}
		return false;
	}
	
	/**
	 * Obtenir les Paris vainqueurs dans cette compétition à partir du vainqueur indiqué
	 * 
	 * @param vainqueur
	 * 
	 */
	public LinkedList<Pari> getParisVainqueurs(String vainqueur) {
		LinkedList<Pari> paris = new LinkedList<Pari>();
		for (Pari pari: this.getParis()) {
			if (pari.getVainqueur().equals(vainqueur)) {
				paris.add(pari);
			}
		}
		return paris;
	}
	
	/**
	 * Obtenir dans une liste, les competitions avec format Nom, Date
	 * 
	 */
	public LinkedList<String> getLinkedListCompetition() {
		LinkedList<String> competition = new LinkedList<String>();
		competition.add(getNom());
		competition.add(getDate().toString());
		return competition;
	}
	
	// ---- Getters ----

	public LinkedList<String> getCompetitors() { return competitors; }

	public DateFrancaise getDate() { return date; }
	
	public String getNom() { return nom; }
	
	public LinkedList<Pari> getParis() { return paris; }

	public boolean getSolde() { return this.solde; }

	// ---- Setters ----
	
	public void setCompetitors(String[] competitors) { this.competitors = new LinkedList(Arrays.asList(competitors)); }

	public void setDate(DateFrancaise date) { this.date = date; }
	
	public void setNom(String nom) {this.nom = nom; }
	
	public void setParis() { this.paris = new LinkedList<Pari>(); }

	public void setSolde(boolean value) { this.solde = value; }

}
