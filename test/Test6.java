

public class Test6 implements Runnable{

    public int test(int a, int[] aa, boolean b, boolean[][] bb ,String c, String[][][] cc) {
        return 0;
    }

    public static void static_test(){}
    private void instance_test() {}

    @Override
    public void run() {}

    public void test() {
        Test6.static_test();
        Test6 t = new Test6();
        t.instance_test();
        super.equals(null);
        this.run();
        ((Runnable)t).run();
    }




    public static void main(String[] args) {
        new Test6().test();
    }
}