class One {
	// two doubles
	double x, y; 
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
		 
	}
}