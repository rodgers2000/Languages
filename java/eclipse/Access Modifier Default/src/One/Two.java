package One;

public class Two {
	// default variable
	int a; 
	public Two(int b){
		a = b; 
	}
	public int getA(){
		return a+10; 
	}
	public void callThree() {
		Three mjr = new Three();
		mjr.getTwoA();
	}
}

class Three {
	public void getTwoA() {
		Two mjr = new Two(10);
		System.out.print(mjr.a);
	}
}