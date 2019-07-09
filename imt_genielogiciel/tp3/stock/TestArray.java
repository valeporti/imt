package stock;

import product.Product;

/**
 * Classe pour tester le stock
 * @author  F. Dagnat et J. Mallet
 */
public class TestArray {
  public static void main(String[] args) {
    System.out.println("Test d'un stock base sur une liste ");
    Stock s = new StockArray(100);

    Product beurre = new Product("Beurre");
    Product lait = new Product("lait");
    Product fromage = new Product("fromage");
    Product jambon1 = new Product("jambon");
    Product jambon2 = new Product("jambon");

    System.out.println("1) Test avec un stock vide");
    System.out.println("\tStock vide ? : " + s.isEmpty());
    System.out.println("\tStock plein ? : " + s.isFull());
    System.out.println("\tTaille du stock : " + s.getSize());
    System.out.println("\tStock : " + s); // Appel de toString()
    s.remove();
    if (s.isEmpty() && !s.isFull() && s.getSize() == 0)
        System.out.println("1 est OK !");
    
    s.add(beurre);
    System.out.println("2) Test stock vide avec stock non vide");
    System.out.println("\tStock vide ? : " + s.isEmpty());
    System.out.println("\tStock : " + s);
    System.out.println("\ts doit contenir du beurre");
    System.out.println("\tOn ajoute du lait : " + lait);
    s.add(lait);
    System.out.println("\tStock : " + s);
    System.out.println("s doit contenir du beurre et du lait, si oui 2 est OK !");
      
    System.out.println("3) Taille avec pas encore de remove");
    System.out.println("\tTaille du stock : " + s.getSize());
    if (s.getSize() == 2) System.out.println("3 est OK !");
      
    System.out.println("4) Test remove sur stock non vide");
    System.out.println("\tOn retire le lait : " + s.remove());
    System.out.println("\tOn ajoute du fromage : " + fromage);
    s.add(fromage);
    System.out.println("\tOn ajoute du jambon : " + jambon1);
    s.add(jambon1);
    System.out.println("\tStock : " + s);
    System.out.println("s doit contenir du beurre, du fromage et du jambon, si oui " +
      		 "4 est OK !");
      
    System.out.println("5) On rajoute et en plus on remplit");
    s.add(jambon1);
    s.add(jambon2);
    System.out.println("\tJ'ajoute " + jambon1 + " et " + jambon2);
    System.out.println("\tStock plein ? : " + s.isFull());
    System.out.println("\tTaille du stock : " + s.getSize());
    System.out.println("\tStock : " + s);
    if (!s.isFull() && s.getSize() == 5) {
       System.out.println("s doit contenir du beurre, du fromage, " +
                          "du jambon, du jambon et du jambon, si oui " +
                          "5 est OK !");
    }
      
  }
}
