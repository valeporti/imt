package siteParis;


public class User {

	/**
	 * @uml.property  name="auth"
	 */
	private boolean auth;

	/**
	 * @uml.property  name="nom"
	 */
	private String nom;

	/**
	 * @uml.property  name="password"
	 */
	private String password;

	/**
	 * @uml.property  name="prenom"
	 */
	private String prenom;

	/**
	 * @uml.property  name="pseudo"
	 */
	private String pseudo;

	/**
	 * @param password TODO
	 */
	public boolean authenticate(String password){
		
		return false;	
	}

			
	/**
	 */
	public boolean comparePassword(){
		return false;	
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
	 * Getter of the property <tt>password</tt>
	 * @return  Returns the password.
	 * @uml.property  name="password"
	 */
	public String getPassword() {
		return password;
	}

	/**
	 * Getter of the property <tt>prenom</tt>
	 * @return  Returns the prenom.
	 * @uml.property  name="prenom"
	 */
	public String getPrenom() {
		return prenom;
	}

	/** 
	 * Getter of the property <tt>username</tt>
	 * @return  Returns the username.
	 * @uml.property  name="pseudo"
	 */
	public String getPseudo() {
		return pseudo;
	}

	/** 
	 * Getter of the property <tt>authentifie</tt>
	 * @return  Returns the authentifie.
	 * @uml.property  name="auth"
	 */
	public boolean isAuth() {
		return auth;
	}

	/** 
	 * Setter of the property <tt>authentifie</tt>
	 * @param authentifie  The authentifie to set.
	 * @uml.property  name="auth"
	 */
	public void setAuth(boolean auth) {
		this.auth = auth;
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
	 * Setter of the property <tt>password</tt>
	 * @param password  The password to set.
	 * @uml.property  name="password"
	 */
	public void setPassword(String password) {
		this.password = password;
	}

	/**
	 * Setter of the property <tt>prenom</tt>
	 * @param prenom  The prenom to set.
	 * @uml.property  name="prenom"
	 */
	public void setPrenom(String prenom) {
		this.prenom = prenom;
	}

	/** 
	 * Setter of the property <tt>username</tt>
	 * @param username  The username to set.
	 * @uml.property  name="pseudo"
	 */
	public void setPseudo(String pseudo) {
		this.pseudo = pseudo;
	}

}
