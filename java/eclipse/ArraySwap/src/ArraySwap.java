
public class ArraySwap {
	public static void main(String[] arg) {
		int [] mjr = new int[] {1, 2, 3, 4};
		int temp = mjr[0];
		mjr[0] = mjr[3]; 
		mjr[3] = temp; 
		for (int i = 0; i < mjr.length; i++) {
			System.out.println(mjr[i]);
		}
	}
}
