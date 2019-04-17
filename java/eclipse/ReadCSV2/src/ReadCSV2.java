import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ReadCSV2 {
	public static void main(String[] args) throws IOException {
		String filepath = "/Users/mrodgers/Documents/other/languages/java/eclipse/ReadCSV/src/data.csv";
		BufferedReader br = new BufferedReader(new FileReader(filepath));
		String line = null; 
		int rows = 2; 
		int cols = 3;
		int row = 0; 
		int col = 0; 
		double A[][] = new double [rows][cols];
		
		while ((line = br.readLine()) != null) {
			String[] values = line.split(",");
			for (String str : values) {
				A[row][col] = Double.parseDouble(str);
				col++; 
			}
			row++; 
			col = 0; 
		}
		
		for(int i = 0; i < rows; i++) {
			for(int j = 0; j < cols; j++) {
				System.out.println(A[i][j]);
			}
		}
		
		
		br.close();
	}
}