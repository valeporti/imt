package squelette;
import java.util.Scanner;


public class Simu {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Aef aef = new Aef2tt(0, new int[] {2,5}); // l'automate a simuler
		Scanner scan = new Scanner(System.in);
		String input;
		while (true){
			System.out.println("Veuillez entrer votre chaine de test");
			input = scan.next();
			if (aef.accepte(input)) System.out.println("La chaine " + input + " est acceptee");
			else System.out.println("La chaine " + input + " n'est PAS acceptee");
		}

	}

}
