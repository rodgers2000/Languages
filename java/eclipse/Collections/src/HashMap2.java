import java.util.HashMap;

public class HashMap2 {
	
	public static void main(String[] args) {
		HashMap mjr = new HashMap();
		mjr.put(1, "one");
		mjr.put(2, "two");
		mjr.put(3, "three");
		
		for(Object key: mjr.keySet()) {
			Object a = mjr.get(key);
			System.out.println(a);
		}
	}
}