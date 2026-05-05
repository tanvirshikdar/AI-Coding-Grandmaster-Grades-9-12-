import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.println("Enter first number (x):");
            int x = Integer.parseInt(scanner.nextLine());

            System.out.println("Enter second number (y):");
            int y = Integer.parseInt(scanner.nextLine());

            int z = x / y;
            System.out.println("Result of division: " + z);

            int[] numbers = new int[2];
            System.out.println("Enter a number to store in array index 0:");
            numbers[0] = Integer.parseInt(scanner.nextLine());
            
            System.out.println("Attempting to access the 3rd element (index 2):");
            System.out.println(numbers[2]);

        } catch (NumberFormatException e) {
            System.out.println("Error: Invalid input. Please enter numeric values only.");
            System.out.println("Details: " + e);
        } catch (ArithmeticException e) {
            System.out.println("Error: Cannot divide by zero.");
            System.out.println("Details: " + e);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Error: Array index is out of range.");
            System.out.println("Details: " + e);
        } catch (Exception e) {
            System.out.println("An unexpected error occurred.");
            System.out.println("Details: " + e);
        } finally {
            scanner.close();
        }
    }
}