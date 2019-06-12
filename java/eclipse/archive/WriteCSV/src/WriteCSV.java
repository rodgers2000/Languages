import java.io.FileWriter;
import java.io.IOException;


public class WriteCSV {
	public static void main(String[] args) throws IOException {
		String file = "/Users/mrodgers/Desktop/test.csv";
		FileWriter writer = new FileWriter(file);
		writer.append("Col1");
		writer.append(",");
		writer.append("Col2");
		writer.append("\n");
		// add data
		writer.append(Integer.toString(1));
		writer.append(",");
		writer.append(Integer.toString(2));
		writer.append("\n");
		writer.close();
	}
}
