import java.util.Scanner;
import java.io.File;

public class ReadCSV {

	public static void main(String[] args) {
		String filepath = "/Users/mrodgers/Documents/other/languages/java/eclipse/ReadCSV/src/data.csv";
        //Get scanner instance
        Scanner scanner = new Scanner(new File(filepath));
         
        //Set the delimiter used in file
        scanner.useDelimiter(",");
         
        //Get all tokens and store them in some data structure
        //I am just printing them
        while (scanner.hasNext())
        {
            System.out.print(scanner.next() + "|");
        }
         
        //Do not forget to close the scanner 
        scanner.close();

	}

}