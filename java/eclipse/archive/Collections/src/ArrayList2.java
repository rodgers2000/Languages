import java.util.ArrayList;

public class ArrayList2 {
	
	@SuppressWarnings({ "rawtypes", "unchecked" })
	public static void main(String[] args) {
		ArrayList mjr = new ArrayList();
		mjr.add(1);
		mjr.add(2);
		mjr.add("Hello");
		for(int i = 0; i < mjr.size(); i++) {
			System.out.println(mjr.get(i));
		}
	}
}