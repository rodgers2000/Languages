import java.util.LinkedList;
import java.util.Queue;

public class Queue2 {

	public static void main(String[] args) {
		Queue<String> mjr = new LinkedList<>();
		mjr.add("a");
		mjr.add("b");
		System.out.println(mjr.remove());
	}

}
