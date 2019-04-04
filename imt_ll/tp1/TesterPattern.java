import java.util.Scanner;
public class TesterPattern {
	
		public static void main(String[] args) {	
		Scanner sc = new Scanner(System.in);
		// Attention : pour mettre un point '.' dans le pattern, il faut le distinguer du point désignant n'importe quel caractere
		// Comme le pattern est dans une chaine de caractere Java, il faut rajouter un deuxième \ pour protéger le premier
		String regex = "[0-9]+\\.[0-9]*"; // un nombre réel
		String chaine;

			do{
				chaine=sc.nextLine();	
				if (chaine.matches(regex)) System.out.println(chaine + "--> OK");
				else System.out.println(chaine + "--> PAS OK");
			} while (sc.hasNext());
		}		
}

	
