package siteParis;

import java.util.Collection;
import java.util.LinkedList;


public class Competition {

	/**
	 * @uml.property  name="nom"
	 */
	private String nom;

	/**
	 * Getter of the property <tt>nom</tt>
	 * @return  Returns the nom.
	 * @uml.property  name="nom"
	 */
	public String getNom() {
		return nom;
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
	 * @uml.property  name="date"
	 */
	private DateFrancaise date;

	/**
	 * Getter of the property <tt>date</tt>
	 * @return  Returns the date.
	 * @uml.property  name="date"
	 */
	public DateFrancaise getDate() {
		return date;
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
	 * @uml.property  name="description"
	 */
	private String description;

	/**
	 * Getter of the property <tt>description</tt>
	 * @return  Returns the description.
	 * @uml.property  name="description"
	 */
	public String getDescription() {
		return description;
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
	 * @uml.property   name="paris"
	 * @uml.associationEnd   multiplicity="(0 -1)" inverse="competition:siteParis.Pari"
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

	/**
	 * @uml.property  name="competitors"
	 */
	private String competitors;

	/**
	 * Getter of the property <tt>competitors</tt>
	 * @return  Returns the competitors.
	 * @uml.property  name="competitors"
	 */
	public String getCompetitors() {
		return competitors;
	}

	/**
	 * Setter of the property <tt>competitors</tt>
	 * @param competitors  The competitors to set.
	 * @uml.property  name="competitors"
	 */
	public void setCompetitors(String competitors) {
		this.competitors = competitors;
	}

	/**
	 * @uml.property  name="siteDeParisMetier"
	 * @uml.associationEnd  inverse="competition:siteParis.SiteDeParisMetier"
	 */
	private SiteDeParisMetier siteDeParisMetier;

	/**
	 * Getter of the property <tt>siteDeParisMetier</tt>
	 * @return  Returns the siteDeParisMetier.
	 * @uml.property  name="siteDeParisMetier"
	 */
	public SiteDeParisMetier getSiteDeParisMetier() {
		return siteDeParisMetier;
	}

	/**
	 * Setter of the property <tt>siteDeParisMetier</tt>
	 * @param siteDeParisMetier  The siteDeParisMetier to set.
	 * @uml.property  name="siteDeParisMetier"
	 */
	public void setSiteDeParisMetier(SiteDeParisMetier siteDeParisMetier) {
		this.siteDeParisMetier = siteDeParisMetier;
	}

}
