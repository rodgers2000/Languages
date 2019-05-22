import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ReadCSV {
	
	public static void main(String[] args) throws FileNotFoundException{ 
		String filepath = "/Users/mrodgers/Documents/other/languages/java/eclipse/archive/ReadCSV/src/data.csv";
        //Get scanner instance
        Scanner scanner = new Scanner(new File(filepath));
         
        //Set the delimiter used in file
        scanner.useDelimiter(",");
        //Get all tokens and store them in some data structure
        //I am just printing them
        while (scanner.hasNext())
        {
        	String mjr = scanner.next();
        	if (mjr.contains("\n")) {
        		 String[] abc = mjr.split("\n");
        		 for(String i:abc) {
        			 System.out.print(i + " ");
        		 }
        	} else {
            System.out.print(mjr + " ");
        	}
         
        //Do not forget to close the scanner 
       }
        scanner.close();
	}
	
}