import java.util.Scanner;

public class RunMe {
	
	static int rows = 2; 
	static int cols = 2; 
	
	static int [][] mjr = new int [rows][cols];
	
	public static void print() {
		for (int i = 0; i < rows; i++) {
			for (int j = 0; j < cols; j++) {
				System.out.print(mjr[i][j]);
			}
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner reader = new Scanner(System.in);
		for (int i = 0; i < rows; i++) {
			for (int j = 0; j < cols; j++) {
				System.out.print("Enter a number: ");
				int n = reader.nextInt();
				mjr[i][j] = n;
			}
		}
		reader.close();
		print();
	}

}
