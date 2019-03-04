import java.util.LinkedList;

public class Section {

	private String title;
	private LinkedList<Paragraph> paragraphs;
	
	public Section (String title, LinkedList<Paragraph> paragraphs) {
		
		this.title = title;
		this.paragraphs = paragraphs;
		
	}
	
	public void addParagraph(Paragraph p) { this.paragraphs.add(p); }
	public String toString() { 
		String paragraph_text = "Section '" + this.title + "'";
		int counter = 0;
		for (Paragraph p : paragraphs) { 
			paragraph_text += "\nParagraph " + (counter ++) + " : ";  
			paragraph_text += p.getParagraph(); 
		}
		return paragraph_text;
	}
	
	public static void main (String[] args) {
		
		Paragraph paragraph = new Paragraph("First Paragraph");
		Paragraph paragraph2 = new Paragraph("Second Paragraph");
		
		LinkedList<Paragraph> list = new LinkedList<Paragraph>();
		
		list.add(paragraph);
		list.add(paragraph2);
		
		Section section = new Section("title",  list);
		
		System.out.println(section.toString());
	}
}
