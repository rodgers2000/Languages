public class Iteration {
	
	public static void main(String[] args) {
		int[] mjr = {1, 2, 3, 4};
		
		for(int i = 0; i < mjr.length; i++) {
			System.out.println(mjr[i]);
		}
		
		for(int i : mjr) {
			System.out.println(i);
		}
		
		int i = 0; 
		while (i < mjr.length) {
			System.out.println(mjr[i]);
			i++;
		}
		
		i = 0; 
		do {
			System.out.println(mjr[i]);
			i++; 
		} while(i < mjr.length);
		
		
	}
}