import java.util.Stack;


public class Stack2 {

	public static void main(String[] args) {
		
		Stack<String> stack = new Stack<> ();
        stack.push("fly");
        stack.push("worm");
        stack.push("butterfly");
        
        System.out.println(stack.pop());
	}

}
