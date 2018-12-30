
public class Test14 implements Cloneable {

    private double pi = 3.14;

    @Override
    public Test14 clone() {
        try {
            return (Test14) super.clone();
        } catch(Exception e) {
            return null;
        }
    }


    public static void main(String[] args) {

        Test14 o1 = new Test14();
        Test14 o2 = o1.clone();
        o2.pi = 3.0;

        System.out.println(o1.pi);
        System.out.println(o2.pi);

    }
}