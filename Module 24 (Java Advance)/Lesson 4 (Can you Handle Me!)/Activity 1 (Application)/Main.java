import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.println("Enter two numbers:");
            int x = scanner.nextInt();
            int y = scanner.nextInt();
            int z = x / y;
            System.out.println(x + " / " + y + " = " + z);
        } catch (ArithmeticException e) {
            System.out.println("--- catch block ---");
            System.out.println(e.toString());
        } finally {
            System.out.println("---- finally block ----");
            System.out.println("Application Designed & Developed by");
            System.out.println("team @ Codingal");
            scanner.close();
        }
        System.out.println("--- DONE ---");
    }
}