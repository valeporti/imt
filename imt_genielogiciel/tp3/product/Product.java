package product;
/**
 * Version avec reference de la classe Product. Un Product possede un
 * nom et un numero qui correspond a son rang de creation. Il est
 * possible de recuperer ce nom, ce numero et de transformer un
 * produit en chaine de caracteres. Il est egalement possible de
 * savoir le nombre de produits deja crees.
 * @authors  F.Dagnat J Mallet
 */
public class Product {
  /** le nom du produit sous forme d'une chaine de caracteres */ 
  private String name;

  /** le nombre de produit deja cree, il permet d'attribuer un numero
   * a chaque produit, ce numero est incremente a chaque
   * instanciation */
  static private int numberCreated = 0;  

  /** Le numero du produit */ 
  private int number;

  /** un constructeur qui prend en parametre le nom du nouveau
   * produit */
  public Product(String name) { 
    this.name = name; 
    number = ++ numberCreated; 
  } 
  /** un constructeur qui prend en parametre le nom du produit et son
   * numero dans ce cas le nombre de produit cree n'est pas
   * incremente*/
  public Product(String name, int number) { 
    this.name = name; 
    this.number = number; 
  } 
   
  /** rend une chaine de caracteres qui est le nom du produit */
  public String getName() { return name; }
   
  /** rend le numero du produit */
  public int getNumber() { return number; }

  /** rend le nombre de produits crees */   	
  public static int getNumberCreated() { return numberCreated; }

  /** compare ce produit avec l'objet specifie
   * @param o l'Objet a comparer avec le Produit courant */    		
  public boolean equals(Object o) {
    if (!(o instanceof Product)) return false;
    Product p = (Product) o;
    return this.name == p.name;
  }
    
  /** rend une chaine de caracteres qui decrit le produit */   	
  public String toString() { return "Produit " + name + " de num " + number; }

  /** Une methode main qui teste cette classe */
  public static void main(String[] args) {
    Product p1 = new Product("p1");
    System.out.println(p1);
    System.out.println("Le nombre de produits crees est " + Product.getNumberCreated());
    new Product("");
    Product p3 = new Product("p3");
    Product p3Bis = new Product("p3",3);
    Product p3Ter = p3;

    if(p3.equals(p3Bis))
	System.out.println("p3 est identique a p3Bis");
    else
	System.out.println("p3 est different de p3Bis");

    if(p3.equals(p3Ter))
	System.out.println("p3 est identique a p3Ter");
    else
	System.out.println("p3 est different de p3Ter");

    if(p3.equals(p1))
	System.out.println("p3 est identique a p1");
    else
	System.out.println("p3 est different de p1");

    System.out.println(p3); 
    System.out.println("Le nom de p3 est " + p3.getName()); 
    System.out.println("Le numero de p3 est " + p3.getNumber()); 
    System.out.println("Le nombre de produits crees est " + Product.getNumberCreated());

    System.out.println("Nous allons creer 12 produits :");
    for(int i = 1; i <= 12; i ++)
      new Product("p" + i);
    System.out.println("Le nombre de produits crees est " + Product.getNumberCreated());
  }
}
