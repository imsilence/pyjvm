
public class Test10 {

    private static void bubble(int[] array) {
        for(int i = 0; i < array.length - 1; i++) {
            for(int j = 0; j < array.length - 1; j++) {
                if(array[j] > array[j + 1]) {
                    int tmp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = tmp;
                }
            }
        }
    }

    private static void print(int[] array) {
        for(int a : array) {
            System.out.println(a);
        }
    }

    public static void main(String[] args) {
        int[] array = {2, 9, 8, 4, 3, 1};
        bubble(array);
        print(array);
    }
}