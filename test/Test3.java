public class Test3 {

    public static int static_var = 1;
    public int instance_var = 2;

    public static void main(String[] args) {
        int x = 3;

        Test3 test3 = new Test3();
        x = test3.static_var;
        test3.instance_var = x;
        x = test3.instance_var;
        Object obj = test3;

        if (obj instanceof Test3) {
            test3 = (Test3) obj;
            System.out.println(test3.static_var);
            System.out.println(test3.instance_var);
        }

    }
}