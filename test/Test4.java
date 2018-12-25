public class Test4 {

    public static int static_var;
    public int instance_var;

    public static void main(String[] args) {
        int x = 32768;

        Test4 test = new Test4();

        Test4.static_var = x;
        x = Test4.static_var;
        test.instance_var = x;
        x = test.instance_var;

        Object obj = test;

        if (obj instanceof Test4) {
            test = (Test4) obj;
            System.out.println(test.instance_var);
        }

    }
}