

public class Test7 {

    private static long fib(long n) {
        if(n <= 1) {
            return n;
        } else {
            return fib(n - 1) + fib(n - 2);
        }
    }

    public static void main(String[] args) {
        long x = fib(10);
        System.out.println(x);
    }
}