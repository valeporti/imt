package siteParis;

import java.util.Collection;
import java.util.LinkedList;
import java.util.Arrays;


public class Competition {

	/**
	 * @uml.property  name="competitors"
	 */
	private LinkedList<String> competitors;

	/**
	 * @uml.property  name="date"
	 */
	private DateFrancaise date;
	
	/**
	 * @uml.property  name="solde"
	 */
	private boolean solde;

	/**
	 * @uml.property  name="description"
	 */
	private String description;

	/**
	 * @uml.property  name="nom"
	 */
	private String nom;

	/**
	 * @uml.property   name="paris"
	 * @uml.associationEnd   multiplicity="(0 -1)" inverse="competition:siteParis.Pari"
	 */
	private LinkedList<Pari> paris;
	
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
		this.description = null;
		this.setSolde(false);
	}
	
	/**
	 * Verifier l'existance d'un compétiteur dnas la liste
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
	 * Getter of the property <tt>competitors</tt>
	 * @return  Returns the competitors.
	 * @uml.property  name="competitors"
	 */
	public LinkedList<String> getCompetitors() {
		return competitors;
	}

	/**
	 * Getter of the property <tt>date</tt>
	 * @return  Returns the date.
	 * @uml.property  name="date"
	 */
	public DateFrancaise getDate() {
		return date;
	}

	/**
	 * Getter of the property <tt>description</tt>
	 * @return  Returns the description.
	 * @uml.property  name="description"
	 */
	public String getDescription() {
		return description;
	}

	/**
	 * Getter of the property <tt>nom</tt>
	 * @return  Returns the nom.
	 * @uml.property  name="nom"
	 */
	public String getNom() {
		return nom;
	}
	
	/**
	 * Verifier si cette compétition a été soldée
	 * 
	 */
	public boolean getSolde() {
		return this.solde;
	}

	/**
	 * Getter of the property <tt>paris</tt>
	 * @return  Returns the paris.
	 * @uml.property  name="paris"
	 */
	public LinkedList<Pari> getParis() {
		return paris;
	}

	/**
	 * Setter of the property <tt>competitors</tt>
	 * @param competitors  The competitors to set.
	 * @uml.property  name="competitors"
	 */
	public void setCompetitors(String[] competitors) {
		this.competitors = new LinkedList(Arrays.asList(competitors));
	}

	/**
	 * Setter of the property <tt>date</tt>
	 * @param date  The date to set.
	 * @uml.property  name="date"
	 */
	public void setDate(DateFrancaise date) {
		this.date = date;
	}

	/**
	 * Setter of the property <tt>description</tt>
	 * @param description  The description to set.
	 * @uml.property  name="description"
	 */
	public void setDescription(String description) {
		this.description = description;
	}
	
	/**
	 * Setter of the property <tt>solde</tt>
	 * @param value  La valeur de soldé.
	 * @uml.property  name="solde"
	 */
	public void setSolde(boolean value) {
		this.solde = value;
	}

	/**
	 * Setter of the property <tt>nom</tt>
	 * @param nom  The nom to set.
	 * @uml.property  name="nom"
	 */
	public void setNom(String nom) {
		this.nom = nom;
	}

	/**
	 * Setter of the property <tt>paris</tt>
	 * @param paris  The paris to set.
	 * @uml.property  name="paris"
	 */
	public void setParis() {
		this.paris = new LinkedList<Pari>();
	}
	
	/**
	 * Ajouter un pari
	 * 
	 * @param p pari à ajouter
	 * 
	 */
	public void addPari(Pari p) {
		this.paris.add(p);
	}
	
	/**
	 * Obtenir les Vainqueurs dans cette compétition à partir d'indiquer le vainqueur
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
	 * Obtenir en forme de liste, les competitions avec format Nom, Date
	 * 
	 */
	public LinkedList<String> getLinkedListCompetition() {
		LinkedList<String> competition = new LinkedList<String>();
		competition.add(getNom());
		competition.add(getDate().toString());
		return competition;
	}

}
