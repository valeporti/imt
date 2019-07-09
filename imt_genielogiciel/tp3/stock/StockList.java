package stock;

import java.util.LinkedList;
import product.Product;

public class StockList implements Stock {
	
	private LinkedList<Product> products;
	
	public LinkedList<Product> getProducts() {
		return this.products;
	}
	
	public void add(Product product) {
		products.add(product);
	}
	
	/** permet de savoir si le stock plein */ 
	public boolean isFull() { return products.size() > 0; }
	
	/** permet de savoir si le stock est vide */
	public boolean isEmpty() { return products.size() == 0; }
	
	/** permet de savoir le nombre d'elements du stock */
	public int getSize() {return products.size(); }
	
	public Product remove() {
	    if(isEmpty()) return null;
	    int sizeof = getSize();
	    return products.remove(sizeof - 1);
	}
	
	public StockList() {
		this.products = new LinkedList<Product>();
	}
	
	public String toString() {
		
		String stock_string = "Stock :";
		int counter = 0;
		for (Product p : products) { 
			stock_string += "\nProduct " + (counter ++) + " : ";  
			stock_string += p.toString(); 
		}
		return stock_string;
	}
	
}
