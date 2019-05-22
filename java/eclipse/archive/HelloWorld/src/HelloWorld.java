import package1.Mike;

class Mike2 extends Mike{
	double x = 10.69;  
	
	Mike2(){
		
	}
	
	double getX(){
		return x; 
	}
	
	int getAAA2() {
		return aaa;
	}
	
}

public class HelloWorld {
	
	public static void main(String[] args) {
		System.out.println("Hello World");
		Mike a = new Mike();
		System.out.println(a.getAAA());
		
		a.talk();
		
		Mike2 b = new Mike2();
		System.out.println(b.x);
		System.out.println(b.getAAA2());
	}
	
}
