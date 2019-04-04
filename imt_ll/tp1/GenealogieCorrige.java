package ExpReg;
import java.util.regex.*;
import java.io.* ;


public class GenealogieCorrige {
	public static void main (String[] args){
		String leFichier = "./src/ExpReg/gen1551.csv";
		String uneLigne;
		String uneLigneTraitee;
		try {
			BufferedReader input = new BufferedReader (new FileReader (leFichier));
			
			while (input.ready()) {
				uneLigne = input.readLine();
				uneLigneTraitee = traiter4b(uneLigne);
				if (!uneLigneTraitee.equals(""))
						System.out.println(uneLigneTraitee);
			}
			input.close();
		}
		catch (FileNotFoundException ex) {
		      System.out.println("Fichier inexistant !!");
		    }
	    catch (IOException ex) {
		      System.out.println("Erreur de lecture du fichier !!");
		    }
	}
		
	public static String traiter (String ligne){
		// Mettre ici le traitement souhait�
		return(ligne);
	}
	
	public static String traiter1 (String ligne){
		// Selectionner toutes  les fiches de personnes prénommées PAUL
		Pattern p = Pattern.compile("^([0-9]+);[^;]*;PAUL;");
		Matcher m = p.matcher(ligne);
		String res="";
		if (m.find())
			// Afficher le numéro de fiche suivi de la fiche entière
			res=(m.group(1)+ " " + ligne);
		return res;
	}
	/* Résultat d'execution traiter1: 
	 * 
	 * 
2030 2030;CABON;PAUL;11/05/1729;PLOUNEVEZ LOCHRIST;25/11/1749;PLOUNEVEZ LOCHRIST;EDERN;FRANCOISE;26/05/1783;PLOUNEVEZ LOCHRIST;;;;;;;
3578 3578;COAT;PAUL;;PLOUGUERNEAU;16/07/1720;PLOUGUIN;SAUX       (LE);LOUISE;;;;;;;;
614 614;GUEDOC;PAUL;; ;23/02/1713;PLOUDALMEZEAU;CROGUENNOC;JEANNE;15/05/1727;LAMPAUL PLOUDALMEZEAU;;;;;;;
3392 3392;GUILLOU;PAUL;; ;;;BRETON     (LE);CATHERINE;;;3488;;;;;;
3488 3488;GUILLOU;PAUL;; ;;;BRETON     (LE);CATHERINE;;;3392;;;;;;
2154 2154;HIR (LE);PAUL;; ;;;MAZE;MARIE;;;;;;;;;
94 94;KERDRAON;PAUL;01/08/1809;DIRINON;21/02/1848;DIRINON;CAROFF;NONNE JEANNE;09/01/1875;DIRINON;;;;;;
376 376;KERDRAON;PAUL;12/08/1756;LOPERHET;20/02/1775;LOPERHET;JEZEQUEL;JEANNE;02/06/1816;LOPERHET;;;;;;
3008 3008;KERDRAON;PAUL;02/11/1687;PLOUGASTEL;24/11/1720;PLOUGASTEL;LAURANS;MARIE;10/12/1745;PLOUGASTEL;;;;;;
2094 2094;KERRENEUR;PAUL;; ;;;MAGUEUR;MARIE;24/09/1696;PLOUDALMEZEAU;;;;;;;
9354 9354;MADEC;PAUL;; ;13/11/1636;PLOUDALMEZEAU;BOZEC;MARGUERITE;;;;;;;;
1148 1148;MARC;PAUL;; ;04/02/1704;LANHOUARNEAU;MARTIN;ANNE;;;;;;;;;
442 442;MARTIN;PAUL;28/04/1752;PLOUDIRY;07/02/1779;PLOUDIRY;MENEZ;MARGUERITE;13/09/1789;PLOUDIRY;;;;;;
1768 1768;MARTIN;PAUL;; ;29/07/1723;LANDIVISIAU;ELLEOUET;MARIE;23/06/1752;LANDIVISIAU;;;;;;;
3536 3536;MARTIN;PAUL;; ;26/11/1671;BODILIS;SALAUN;MAGDELAINE;30/09/1680;BODILIS;;;;;;;
4114 4114;MASSON;PAUL;; ;;;TREBAOL;FRANCOISE;02/03/1689;LANDUNVEZ;;;;;;
2598 2598;MESGUEN;PAUL;;PLOUESCAT;30/01/1695;KERLOUAN;CABON;ANNE;21/02/1719;PLOUESCAT;;;;;;;
2084 2084;MOREL;PAUL;20/09/1621;LAMPAUL PLOUDALMEZEAU;;;VAILLANT;MARIE;29/01/1681;LAMPAUL PLOUDALMEZEAU;6004;5072;;;;;
5072 5072;MOREL;PAUL;20/09/1621;LAMPAUL PLOUDALMEZEAU;;;VAILLANT;MARIE;29/01/1681;LAMPAUL PLOUDALMEZEAU;6004;2084;;;;;
6004 6004;MOREL;PAUL;20/09/1621;LAMPAUL PLOUDALMEZEAU;;;VAILLANT;MARIE;29/01/1681;LAMPAUL PLOUDALMEZEAU;2084;5072;;;;;
2024 2024;PAGE;PAUL;17/01/1707;PLOUNEVEZ LOCHRIST;24/10/1741;PLOUNEVEZ LOCHRIST;OLIVIER;JEANNE;;;;;;;;;
3226 3226;PERROT;PAUL;; ;;;NICOLAS;JEANNE;;;;;;;;
7826 7826;POULIQUEN;PAUL;; ;;;COAT;MARGUERITE;;;;;;;;
2530 2530;QUEMENEUR;PAUL;; ;31/03/1677;PLOURIN PLOUDALMEZEAU;MARZIN;BARBE;07/07/1713;PLOUDALMEZEAU;;;;;;;
41580 41580;ROSEC;PAUL;;;;;PRISER;MARIE;14/01/1619;CLEDER;;;;;;
12728 12728;ROUX (LE);PAUL;; ;24/10/1616;LE TREHOU;SALAUN;MAGDELAINE;09/04/1661;LE TREHOU;;;;;;
7074 7074;SALAUN;PAUL;; ;;;;;;;;;;;;;
4512 4512;SALOU;PAUL;;;;;CLOAREC;MARIE;;;10448;;;;;;
10448 10448;SALOU;PAUL;;;;;CLOAREC;MARIE;;;4512;;;;;;
1018 1018;TREGUER;PAUL;10/01/1738;BODILIS;04/02/1762;PLOUGAR;ABHERVE-GUEGUEN;FRANCOISE;;;;;;;;;
4072 4072;TREGUER;PAUL;;BODILIS;16/07/1703;BODILIS;GLAS       (LE);CATHERINE;12/06/1713;BODILIS;;;;;;;

	 */
	
	public static String traiter2 (String ligne){
		// Selectionner toutes  les fiches de personnes prénommées PAUL et nées à PLOU.....
		Pattern p = Pattern.compile("^([0-9]+);[^;]*;PAUL;[^;]*;PLOU");
		Matcher m = p.matcher(ligne);
		String res="";
		if (m.find())
			// Afficher le numéro de fiche suivi de la fiche entière
			res=(m.group(1)+ " " + ligne);
		return res;
	}
	
	/* Résultat d'execution traiter2: 
	 * 
	 * 
2030 2030;CABON;PAUL;11/05/1729;PLOUNEVEZ LOCHRIST;25/11/1749;PLOUNEVEZ LOCHRIST;EDERN;FRANCOISE;26/05/1783;PLOUNEVEZ LOCHRIST;;;;;;;
3578 3578;COAT;PAUL;;PLOUGUERNEAU;16/07/1720;PLOUGUIN;SAUX       (LE);LOUISE;;;;;;;;
3008 3008;KERDRAON;PAUL;02/11/1687;PLOUGASTEL;24/11/1720;PLOUGASTEL;LAURANS;MARIE;10/12/1745;PLOUGASTEL;;;;;;
442 442;MARTIN;PAUL;28/04/1752;PLOUDIRY;07/02/1779;PLOUDIRY;MENEZ;MARGUERITE;13/09/1789;PLOUDIRY;;;;;;
2598 2598;MESGUEN;PAUL;;PLOUESCAT;30/01/1695;KERLOUAN;CABON;ANNE;21/02/1719;PLOUESCAT;;;;;;;
2024 2024;PAGE;PAUL;17/01/1707;PLOUNEVEZ LOCHRIST;24/10/1741;PLOUNEVEZ LOCHRIST;OLIVIER;JEANNE;;;;;;;;;

	 */
	
	public static String traiter3 (String ligne){
		// Selectionner toutes  les fiches de personnes prénommées PAUL et nées à PLOU..... 
		// et afficher en changeant le préfixe de la commune de naissance en LOC...
		Pattern p = Pattern.compile("^(([0-9]+);[^;]*;PAUL;[^;]*;)PLOU(.*)");
		Matcher m = p.matcher(ligne);
		String res="";
		if (m.find())
			// Afficher le numéro de fiche, le début de fiche jusqu'à la ville, LOC, puis la fin de la fiche
			res=(m.group(2)+ " " + m.group(1) + "LOC" + m.group(3));
		return res;
	}
	
	/* Résultat d'execution traiter3: 
	 * 
	 * 
2030 2030;CABON;PAUL;11/05/1729;LOCNEVEZ LOCHRIST;25/11/1749;PLOUNEVEZ LOCHRIST;EDERN;FRANCOISE;26/05/1783;PLOUNEVEZ LOCHRIST;;;;;;;
3578 3578;COAT;PAUL;;LOCGUERNEAU;16/07/1720;PLOUGUIN;SAUX       (LE);LOUISE;;;;;;;;
3008 3008;KERDRAON;PAUL;02/11/1687;LOCGASTEL;24/11/1720;PLOUGASTEL;LAURANS;MARIE;10/12/1745;PLOUGASTEL;;;;;;
442 442;MARTIN;PAUL;28/04/1752;LOCDIRY;07/02/1779;PLOUDIRY;MENEZ;MARGUERITE;13/09/1789;PLOUDIRY;;;;;;
2598 2598;MESGUEN;PAUL;;LOCESCAT;30/01/1695;KERLOUAN;CABON;ANNE;21/02/1719;PLOUESCAT;;;;;;;
2024 2024;PAGE;PAUL;17/01/1707;LOCNEVEZ LOCHRIST;24/10/1741;PLOUNEVEZ LOCHRIST;OLIVIER;JEANNE;;;;;;;;;

	 */
	
	
	public static String traiter4 (String ligne){
		// Selectionner toutes  les fiches de personnes prénommées PAUL et nées à PLOU.....
		// et incrémenter de 10 l'année de naissance
		Pattern p = Pattern.compile("^(([0-9]+);[^;]*;PAUL;([0-9]{2}/[0-9]{2}/)?)([0-9]{4})?(;PLOU.*)");
		Matcher m = p.matcher(ligne);
		String res="";
		int annee ;
		if (m.find()){
			if (m.group(3)!=null){
				// la date de naissance est précisee dans la fiche
				annee = new Integer(m.group(4)) + 10;
				res= m.group(2)+ " " + m.group(1) + annee + m.group(5);
			}
			else {
				// la date de naissance n'est pas précisée dans la fiche
				res= m.group(2)+ " " + m.group(1) + m.group(5);
			}
		}
		return res;
	}
	

	public static String traiter4b (String ligne){
		// Selectionner toutes  les fiches de personnes prénommées PAUL et nées à PLOU.....
		// et incrémenter de 10 l'année de naissance
		// Variante de traiter4
		Pattern p = Pattern.compile("^(([0-9]+);[^;]*;PAUL;)([^;]*)(;PLOU.*)");
		Matcher m = p.matcher(ligne);
		String res="";
		int annee ;
		if (m.find()){
			String dateNaissance = m.group(3);
			String nouvelleDate = "";
			if (dateNaissance.matches("[0-9]{2}/[0-9]{2}/[0-9]{4}")) {
				annee= new Integer(dateNaissance.substring(6,10)) +10;
				nouvelleDate= dateNaissance.substring(0,6) + annee;
			}
			res = m.group(2) + " " + m.group(1) + nouvelleDate + m.group(4);
		}
		return res;
	}
	
	/* Résultat d'execution traiter4 et traiter4b: 
	 * 
	 * 
2030 2030;CABON;PAUL;11/05/1739;PLOUNEVEZ LOCHRIST;25/11/1749;PLOUNEVEZ LOCHRIST;EDERN;FRANCOISE;26/05/1783;PLOUNEVEZ LOCHRIST;;;;;;;
3578 3578;COAT;PAUL;;PLOUGUERNEAU;16/07/1720;PLOUGUIN;SAUX       (LE);LOUISE;;;;;;;;
3008 3008;KERDRAON;PAUL;02/11/1697;PLOUGASTEL;24/11/1720;PLOUGASTEL;LAURANS;MARIE;10/12/1745;PLOUGASTEL;;;;;;
442 442;MARTIN;PAUL;28/04/1762;PLOUDIRY;07/02/1779;PLOUDIRY;MENEZ;MARGUERITE;13/09/1789;PLOUDIRY;;;;;;
2598 2598;MESGUEN;PAUL;;PLOUESCAT;30/01/1695;KERLOUAN;CABON;ANNE;21/02/1719;PLOUESCAT;;;;;;;
2024 2024;PAGE;PAUL;17/01/1717;PLOUNEVEZ LOCHRIST;24/10/1741;PLOUNEVEZ LOCHRIST;OLIVIER;JEANNE;;;;;;;;;

	 */
	
	public static int NbAbalain = 0;
	public static String traiter5 (String ligne){
		// Compter le nombre de fiches ABALAIN
		Pattern p = Pattern.compile("^([0-9]+);ABALAIN;");
		Matcher m = p.matcher(ligne);
		String res="";
		if (m.find()){
			NbAbalain++;
			res=(NbAbalain+ " " + ligne);
		}
		return res;
	}
	
	/* Résultat d'exécution traiter 5
	 * 
1 652;ABALAIN;GOULVEN;17/11/1732;KERLOUAN;07/10/1761;KERLOUAN;SALOU;CATHERINE;20/12/1806;KERLOUAN;;;;;;;
2 1304;ABALAIN;GOULVEN;; ;01/07/1728;KERLOUAN;HABASQUE;LOUISE;23/02/1758;KERLOUAN;;;;;;;
3 2608;ABALAIN;GOULVEN;; ;01/10/1689;PLOUNEOUR TREZ;HABASQUE;CATHERINE;;;;;;;;;
4 14250;ABALAIN;HERVE;01/05/1617;LA MARTYRE;;;TRAOUNGOUEZ;MARIE;09/11/1681;LA MARTYRE;15530;;;;;;
5 15530;ABALAIN;HERVE;01/05/1617;LA MARTYRE;;;TRAOUNGOUEZ;MARIE;09/11/1681;LA MARTYRE;14250;;;;;;
6 326;ABALAIN;JEAN;20/03/1766;KERLOUAN;22/07/1789;KERLOUAN;ABIVEN;MARIE ANNE;24/01/1848;KERLOUAN;;;;;;;
7 28500;ABALAIN;MARC;; ;;;POTART;BEATRICE;;;31060;;;;;;
8 31060;ABALAIN;MARC;; ;;;POTART;BEATRICE;;;28500;;;;;;
9 1113;ABALAIN;MARGUERITE;; ;;;BROUDIN;JEAN;;;;;;;;;
10 7125;ABALAIN;MARGUERITE;01/02/1653;LA MARTYRE;28/07/1674;LA MARTYRE;MOIGN      (LE);FRANCOIS;;;7765;;;;;;
11 7765;ABALAIN;MARGUERITE;01/02/1653;LA MARTYRE;28/07/1674;LA MARTYRE;MOIGN      (LE);FRANCOIS;;;7125;;;;;;
12 5277;ABALAIN;MARIE;; ;;;KERBRAT;SALOMON;;;;;;;;;
13 163;ABALAIN;MARIE JOSEPHE;03/03/1792;KERLOUAN;13/07/1809;KERLOUAN;LOAEC;GUILLAUME;;;;;;;;;

	 */
	
}
