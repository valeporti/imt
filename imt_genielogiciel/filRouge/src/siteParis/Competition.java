package siteParis;

import java.util.Collection;
import java.util.LinkedList;


public class Competition {

	/**
	 * @uml.property  name="competitors"
	 */
	private String[] competitors;

	/**
	 * @uml.property  name="date"
	 */
	private DateFrancaise date;

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
	
	public Competition (String nom, DateFrancaise dateCloture, String [] competiteurs) {
		this.setNom(nom);
		this.setDate(dateCloture);
		this.paris = new LinkedList<Pari>();
		this.setCompetitors(competiteurs);
		this.description = null;
	}

	/**
	 * Getter of the property <tt>competitors</tt>
	 * @return  Returns the competitors.
	 * @uml.property  name="competitors"
	 */
	public String[] getCompetitors() {
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
		this.competitors = competitors;
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
	public void setParis(LinkedList<Pari> paris) {
		this.paris = paris;
	}


}
