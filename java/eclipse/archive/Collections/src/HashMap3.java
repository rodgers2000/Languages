import java.util.HashMap;
import java.util.Map;

public class HashMap3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Map <Integer, Integer> mjr = new HashMap<Integer, Integer>();
		mjr.put(1, 2);
		mjr.put(2, 3);
		for (Map.Entry<Integer, Integer> entry : mjr.entrySet()) {
			if (entry.getKey() == 1) {
				System.out.println(entry.getKey());
				System.out.println(entry.getValue());
			}
		}
	}

}
