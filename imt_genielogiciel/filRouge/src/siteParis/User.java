package siteParis;


public class User {

	/**
	 * Contient le nom de l'Utilisateur
	 */
	private String nom;

	/**
	 * Contient le prenom de l'Utilisateur
	 */
	private String prenom;

	/**
	 * Contient le pseudo de l'Utilisateur
	 */
	private String pseudo;
	
	// ---- Getters ----
	
	public String getNom() { return nom; }

	public String getPrenom() { return prenom; }

	public String getPseudo() { return pseudo; }

	// ---- Setters ----
	
	public void setNom(String nom) { this.nom = nom; }

	public void setPrenom(String prenom) { this.prenom = prenom; }

	public void setPseudo(String pseudo) { this.pseudo = pseudo; }

}
