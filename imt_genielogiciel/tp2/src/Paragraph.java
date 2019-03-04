
public class Paragraph {
	
	private String text;
	
	public Paragraph(String text) { this.text = text; }
	
	public String getParagraph() { return this.text; }
	
	public static void main (String[] args) {
		Paragraph paragraph = new Paragraph("First Paragraph");
		System.out.println("Paragraph: " + paragraph.getParagraph());
	}
}
