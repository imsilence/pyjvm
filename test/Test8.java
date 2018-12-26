
public class Test8 {

    private static long id = 0;

    public static long get_id() {
        Test8.id ++;
        return Test8.id;
    }

    public static void main(String[] args) {
        Test8.get_id();
        Test8.get_id();
        Test8.get_id();
        Test8.get_id();
        Test8.get_id();
        System.out.println(Test8.get_id());
    }
}