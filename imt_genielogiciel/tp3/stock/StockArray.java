package stock;

import product.Product;
/**
 * Je gere un stock d'objets instance de Product sous la forme d'un tableau.
 * J'implemente l'interface Stock. Ma taille est fixee a ma creation.
 * @authors A.Beugnard R.Ogor F.Dagnat J. Mallet
 */
public class StockArray implements Stock {
  /** le tableau contenant les produits */ 
  private Product[] content;

  /** nombre de produits dans le stock */
  private int size; 
    
  /** Construit un stock dont la capacite est donnee par s
   * @param s la taille du stock  */
  public StockArray(int s) {
    content = new Product[s];
    size = 0;
  }
    
  /** rajoute un nouveau produit dans le stock
   * @param p  le produit qui est rajoute  */  
  public void add(Product p)  {
      if (isFull()) return;  
    content[size++] = p;
  }
  
  /** retire le <b>dernier</b> produit ajoute au stock et le rend en
   * resultat */ 
  public Product remove() {
    if(isEmpty()) return null;
    return content[--size];
  }
  

  /** permet de savoir si le stock plein */ 
  public boolean isFull() { return size == content.length; }

  /** permet de savoir si le stock est vide */
  public boolean isEmpty() { return size == 0; }

  /** permet de savoir le nombre d'elements du stock */
  public int getSize() {return size; }
  
  /** rend une chaine de caracteres decrivant le stock */ 
  public String toString() {
    if (isEmpty()) return "Le stock est vide.";
    String s = "Le stock contient : ";
    for (int i = 0; i < size; i++)
      s += "\n\t" + content[i];
    return s;
  }
   
  public static void main(String[] args) {
      Stock s = new StockArray(8);
      System.out.println("Stock Vide : " + s.isEmpty()); 
      System.out.println("Stock Plein : "+ s.isFull());
      System.out.println(s); 
      s.add(new Product("p1"));
      System.out.println("Stock Vide : " + s.isEmpty()); 
      System.out.println(s);
      s.add(new Product("p2"));
      System.out.println(s);
      System.out.println(s.remove() + " est retire du stock !");
      Product p = new Product("p3");
      s.add(p);
      System.out.println(s);
      System.out.println(p + " est retire du stock !");
      s.remove();
      System.out.println(s);
      
      System.out.println("Nous allons ajouter 13 produits dans le stock.");
      int num = 0;
      for(int i = 1; i <= 13; i++) {
	if (!s.isFull()) {
	  s.add(new Product("ppp"+i));
	  num++;
	}
      }
      System.out.println(s);
      System.out.println("En fait, nous avons ajoute " + num + " produits.");
  }
}
