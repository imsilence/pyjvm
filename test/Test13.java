
public class Test13 {


    public static void main(String[] args) {

        Object o1 = new Test13();
        Object o2 = new Test13();

        System.out.println(o1.hashCode());
        System.out.println(o2.hashCode());
        System.out.println(o1.toString());
        System.out.println(o2.toString());
        System.out.println(o1.equals(o2));
        System.out.println(o1.equals(o1));

    }
}