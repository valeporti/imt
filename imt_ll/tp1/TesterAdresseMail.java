package ExpReg;
import java.util.*;


public class TesterAdresseMail {
	


	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		while (true) {
			System.out.println("Veuillez entrer votre chaine de test");
			String input = scan.next();	
			// Attention : pour mettre un point '.' dans le pattern, il faut le distinguer du point désignant n'importe quel caractere
			// Comme le pattern est dans une chaine de caractere Java, il faut rajouter un deuxième \ pour protéger le premier
			if (input.matches("[^@]+@[a-zA-Z]+\\.[a-z]{2,3}")) System.out.println ("La chaine " + input + " ressemble a une adresse electronique");
			else System.out.println ("La chaine " + input + " ne ressemble PAS a une adresse electronique");
			}
	}

}
