import java.util.Random;

public class Matrix {
	public static void main(String[] args) {
		int rows = 10; 
		int cols = 10; 
		double [][] mjr = new double[rows][cols];
		
		Random rand = new Random();
		
		for(int i = 0; i < rows; i++) {
			for (int j = 0; j < cols; j++) {
				mjr[i][j] = rand.nextGaussian();
			}
		}
		for(int i = 0; i < rows; i++) {
			for (int j = 0; j < cols; j++) {
				System.out.println(mjr[i][j]);
			}
		}
		
	}
}