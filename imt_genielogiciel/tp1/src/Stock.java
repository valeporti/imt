/**
 * Un stock d'instances de Product dont la taille est fixee a la creation.
 * @author F.Dagnat
 */
public class Stock {
  /** le tableau contenant les produits */ 
  private Product[]  content;
  /** le nombre de produits deposes */  
  private int size = 0;
  
  /** un constructeur avec comme parametre la taille du stock
   * @param s la taille du stock */  
  public Stock(int s) { content = new Product[s]; }
  
  /** rajoute un nouveau produit dans le stock
   * @param p  le produit qui est rajoute */  
  public void add(Product p){
    if (p==null) return;
    content[size++] = p;
  }
  
  /** retire le <b>dernier</b> produit ajoute au stock et le rend en resultat */ 
  public Product remove() { return content[--size]; }
  
  /** permet de savoir si le stock est vide */ 
  public boolean isEmpty() { return size == 0; }
  
  /** permet de savoir si le stock plein */ 
  public boolean isFull() { return size == content.length; }
  
  /** permet de connaitre le nombre de produits dans le stock */ 
  public int getSize() { return size; }
  
  /** rend une chaine de caracteres decrivant le stock */ 
  public String toString() {
    if (isEmpty()) return "Le stock est vide.";
    String s = "Le stock contient : ";
    for (int i = 0; i < size; i++)
      s += "\n\t" + content[i];
    return s;
  }
  
  /** Une methode main qui teste cette classe */
  public static void main(String[] args) {
    Stock s = new Stock(8);
    System.out.println("Stock Vide : " + s.isEmpty() + ", Stock Plein : "+ s.isFull());
    System.out.println(s); 
    s.add(new Product("p1"));
    System.out.println("Stock Vide : " + s.isEmpty()); 
    System.out.println(s);
    s.add(new Product("p2"));
    System.out.println(s);
    System.out.println(s.remove() + " est retire du stock !");
    s.add(new Product("p3"));
    System.out.println(s);
    System.out.println("Nous allons ajouter 13 produits dans le stock.");
    int num = 0;
    for(int i = 1; i <= 13; i++) {
      if (!s.isFull()) { s.add(new Product("ppp"+i)); num++; }
    }
    System.out.println(s);
    System.out.println("En fait, nous avons ajoute " + num + " produits.");
  }
}
