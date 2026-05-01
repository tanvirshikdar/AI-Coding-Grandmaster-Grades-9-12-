public class main {
    public static void main(String[] args) {
        int number = 532;
        int reversed = 0;

        while (number != 0) {
            int digit = number % 10;
            reversed = reversed * 10 + digit;
            number /= 10;
        }

        System.out.println("Reversed Number: " + reversed);
    }
}