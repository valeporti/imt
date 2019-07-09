package product;

import date.*;
/**
 * Un produit perissable etend la notion de produit en ajoutant une
 * date limite de consommation.  Elle ajoute egalement les methodes
 * pour gerer cette date.
 * @authors  F.Dagnat P.Geffroy
 */
public class PerishableProduct extends Product {
  /** Chaque produit perissable a un date de peremption */
  private Date bestBeforeDate;
    
  /** Un constructeur creant le produit et lui affectant une date de
   * peremption
   * @param  name le nom du nouveau produit 
   * @param  bestBeforeDate la date de peremption */
  public PerishableProduct(String name, Date bestBeforeDate) { 
    super(name);
    this.bestBeforeDate = bestBeforeDate; 
  }
    
  /** indique si le produit est perime */
  public boolean isOutOfDate(){ return bestBeforeDate.before(new Date()); }  
    
  /** retourne la date de peremption. */
  public Date getBestBeforeDate(){ return  bestBeforeDate; }  
	
  /** methode standard qui transforme un objet en chaine de
   * caracteres. */
  public String toString() { 
    return super.toString() + " sera perime le " + bestBeforeDate; 
  }
   
  public static void main(String[] args) {
      Date d1 = new Date(2006, 8, 22);
      Date d2 = new Date(2006, 10, 1);
      Date d3 = new Date(2006, 10, 15);
      PerishableProduct p1 = new PerishableProduct("beurre", d1);
      System.out.println(p1);
      System.out.println("NombreproduitCrees ==  " + Product.getNumberCreated());
      PerishableProduct p2 = new PerishableProduct("lait", d2);
      PerishableProduct p3 = new PerishableProduct("fromage", d2);
      if(p1.isOutOfDate())
	System.out.println(p1 + " est perime aujourd'hui le " + new Date());
      else
	System.out.println(p1 + " n'est pas perime le "+ new Date());
      if(p2.isOutOfDate())
	System.out.println(p2 + " est perime aujourd'hui le " + new Date());
      else
	System.out.println(p2 + " n'est pas perime le "+ new Date());
      System.out.println(p1);
      System.out.println(p3);
      System.out.println("numero de p3  :" + p3.getNumber());
      System.out.println("Nombre de produits crees =  " + Product.getNumberCreated());
      System.out.println("Le produit  " + p3.getName() + " sera perime le " +
			 p3.getBestBeforeDate());
  }
}
