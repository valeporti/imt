import java.util.regex.*;

public class Utilisation {
	
	public static void main (String[] args) {
		Pattern p = Pattern.compile("a*b|c");
		String entree = "aabbbcab";
		Matcher m = p.matcher(entree);
		while (m.find())
			System.out.println(entree.substring(m.start(), m.end()));
	}
	
}