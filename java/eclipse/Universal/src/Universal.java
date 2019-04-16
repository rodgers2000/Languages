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
	public static void main(String[] args) {
		System.out.println("Hello");
		One mjr = new One(10, 69); 
		mjr.print(); 
		System.out.println(mjr.x);
		One.mjr += 1; 
		System.out.println(mjr.mjr);
		
		for (int i : mjr.a) {
			System.out.println(i);
		}
		 
	}
}