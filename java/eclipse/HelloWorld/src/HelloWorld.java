import package1.Mike;

class Mike2 {
	double x = 10.69;  
	
	double getX(){
		return x; 
	}
	
}

public class HelloWorld {
	
	public static void main(String[] args) {
		System.out.println("Hello World");
		Mike a = new Mike();
		System.out.println(a.aaa);
		a.talk();
		
		Mike2 b = new Mike2();
		System.out.println(b.x);
	}
	
}
