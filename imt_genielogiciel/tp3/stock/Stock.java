package stock;

import product.Product;
/**
 * Je gere un stock d'objets instances de Product
 * @author F.Dagnat
 */
public interface Stock {
   
  /** permet de savoir si le stock est vide */ 
  public boolean isEmpty();
  
  /** permet de connaitre le nombre de produits dans le stock */ 
  public int getSize();
  
  /** rajoute un produit dans le stock 
   * @param p le produit qui est rajoute  
   */  
    public void add(Product p);
    
  /** retire le <b>dernier</b> produit ajoute au stock et le rend en
   * resultat */ 
  public Product remove();

  /** permet de savoir si le stock plein */ 
  public boolean isFull(); 
   
  /** rend une chaine de caracteres decrivant le stock */ 
  public String toString();
}
