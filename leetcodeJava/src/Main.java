import java.util.Stack;

public class Main {

    public static void main(String[] args) {
        Stack s = new Stack();

        String s1 = "a\":\"";
        String s2 = "\":\"a";
        String[] l1 = s1.split("\":\"");
        String[] l2 = s2.split("\":\"");
        for (String e : l1) {
            System.out.println("这个元素为" + e);
        }
    }
}
