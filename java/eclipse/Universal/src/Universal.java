class One {
	// two doubles
	double x, y; 
	// static
	int [] a = new int[3];
	static int mjr = 69; 
	/*
	 * Multi line comment
	 * goes like this
	 * amen!!!
	 */
	
	One(double a, double b) {
	x = a; 
	y = b;  
	}
	
	void print(){
		System.out.println("x: " + x);
		System.out.println("y: " + y);
	}
}


public class Universal{
	double x = 0; 
	int [] y = {1, 2, 3};
	
	public static void main(String[] args) {
		Universal mjr = new Universal();
		mjr.printme(mjr);
	}
	
	public void printme(Universal mjr) {
		for(int i : mjr.y) {
			System.out.println(i);
		}
	}
}