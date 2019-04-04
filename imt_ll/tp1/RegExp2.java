import java.util.regex.*;
import java.util.Scanner;

public class RegExp2 {


		/**
		 * 
		 * Le traitement execute dans ce programme demandera beaucoup de temps, 
		 * ce qui illustre les limites d'utilisation des expressions régulieres.
		 */
		public static void main(String[] args) {
		
			try{
				
				String chaine = "ababaabababaababaaababababababbaaaaabababababababababbabababababc";
				if (chaine.matches("(a*ba*)*")) System.out.println(chaine + "--> OK");
					else System.out.println(chaine + "--> PAS OK");
					
				
			}
			catch (PatternSyntaxException pse){System.out.println("Pb de syntaxe du pattern");
		
		}
		
		}

}

