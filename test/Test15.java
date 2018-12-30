
public class Test15 extends RuntimeException {

    public static void test(String[] args) {
        try {
            test2(args);
        } catch(NumberFormatException e) {
            System.out.println(e);
        }
    }

    public static void test2(String[] args) {
        if(args.length == 0) {
            throw new IndexOutOfBoundsException("no args");
        }
        int x = Integer.parseInt(args[0]);
        System.out.println(x);
    }

    public static void main(String[] args)  {
        test(args);
    }
}