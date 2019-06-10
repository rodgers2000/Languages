import java.util.Vector;;


public class Vector2 {

	@SuppressWarnings({ "rawtypes", "unchecked" })
	public static void main(String[] args) {
		
		Vector mjr = new Vector();
		mjr.add(1);
		mjr.add("a");
		System.out.println(mjr);
		
		for (int i = 0; i < mjr.size(); i++) {
			System.out.println(mjr.get(i));
		}

	}

}
