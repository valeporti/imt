

/**
 * 
 * Class Producer
 * 
 * @author s18rames
 *
 */
public class Producer {
	
	/** Nom du producteur */
	private String name;
	/** variable avec le stock appartenant au producteur */
	private Stock myStock;
	
	/**
	 * 
	 * Constructor of Class Producer
	 * 
	 * @param n String name
	 * @param s Stock Object
	 *
	 */
	public Producer (String n, Stock s) {
		name = n;
		myStock = s;
	}
	
	public String getName() { return name; }
	public Stock getStock() { return myStock;}
	public String toString() { return "Producer is " + name + " with stock " + myStock; }
	
	public void setName(String name) { this.name = name; }
	
	public void produce (String productName) {
		Product p1 = new Product(productName);
		this.myStock.add(p1);
	}	
	
	public static void main (String[] args) {
		
		Stock s = new Stock(3);
		Producer producer = new Producer("Producer1", s);
		
		System.out.println("Producer Name : " + producer.getName() + ", Producer Stock : "+ producer.getStock() + ", Producer Desc : " + producer.toString());
	    System.out.println(producer); 
	    
	    producer.setName("new Producer");
	    
	    System.out.println("Producer new name: " + producer.getName());
	    
	    producer.produce("new Product");
	    
	    System.out.println("Producer Name : " + producer.getName() + ", Producer Stock : "+ producer.getStock() + ", Producer Desc : " + producer.toString());
	    System.out.println(producer); 
	    
	}
}
