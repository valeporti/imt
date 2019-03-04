import java.util.LinkedList;

public class Document {
	
	private String title;
	private LinkedList<Section> sections;
	private int currentSection;
	
	public Document(String t) {
		title = t;
		sections = new LinkedList<Section>();
	}
	
	public void nextSection() { this.currentSection ++; }
	public void prevSection() { this.currentSection --; }
	public int currentSection() { return currentSection; }
	public void addSection(Section s) { sections.add(currentSection, s); }
	public String toString() { 
		String document_string = "Document '" + title + "'";
		int counter = 0;
		for (Section s : sections) { 
			document_string += "\nSection " + (counter ++) + " : ";  
			document_string += s.toString(); 
		}
		return document_string;
	}
	
	public static void main (String[] args) {
		
		Paragraph paragraph = new Paragraph("First Paragraph");
		Paragraph paragraph2 = new Paragraph("Second Paragraph");
		Paragraph paragraph3 = new Paragraph("third Paragraph");
		
		LinkedList<Paragraph> list1 = new LinkedList<Paragraph>();
		LinkedList<Paragraph> list2 = new LinkedList<Paragraph>();
		
		list1.add(paragraph);
		list1.add(paragraph2);
		list2.add(paragraph3);
		
		Section section1 = new Section("Sec1",  list1);
		Section section2 = new Section("Sec2",  list2);
		
		Document doc = new Document("doc1");
		doc.addSection(section1);
		doc.addSection(section2);
		
		System.out.println(doc.toString());
	}

}
