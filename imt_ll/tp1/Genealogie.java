import java.util.regex.*;
import java.io.* ;


public class Genealogie {
	public static void main (String[] args){
		String leFichier = "./gen1551.csv";
		String uneLigne;
		String uneLigneTraitee;
		try {
			BufferedReader input = new BufferedReader (new FileReader (leFichier));
			
			int count = 0;
			while (input.ready()) {
				uneLigne = input.readLine();
				uneLigneTraitee = traiter(uneLigne);
				if (!uneLigneTraitee.equals("")) {
					System.out.println(uneLigneTraitee);
					count ++;
				}
			}
			input.close();
			System.out.println("Il y a " + count + " lignes avec ABALAIN");
		}
		catch (FileNotFoundException ex) {
		      System.out.println("Fichier inexistant !!");
		    }
	    catch (IOException ex) {
		      System.out.println("Erreur de lecture du fichier !!");
		    }
	}
		
	public static String traiter (String ligne){
		// Mettre ici le traitement souhaité
		// Pattern p = Pattern.compile("^([0-9]+);([^;]*);([^;]*);([^;]*);(PLOU[^;]*);(.*)");
		// Pattern p = Pattern.compile("^([0-9]+);([^;]*);([^;]*);([0-9]{1,2})/([0-9]{1,2})/([0-9]{4});(.*)");
		Pattern p = Pattern.compile("[.]*ABALAIN[.]*");
		Matcher m = p.matcher(ligne);
		String res = "";
		if (m.find())			
			// res = (m.group(1) + "; " + m.group(2) + "; " + m.group(3) + "; "  + m.group(4) + "; " + m.group(5).replace("PLOU", "LOC") + "; " + m.group(6));
			// res = (m.group(1) + "; " + m.group(2) + "; " + m.group(3) + "; "  + m.group(4) + "; " + m.group(5) + "; " + (Integer.parseInt(m.group(6)) + 10) + "; " + m.group(7));
			res = (ligne);
		return(res);
	}
}