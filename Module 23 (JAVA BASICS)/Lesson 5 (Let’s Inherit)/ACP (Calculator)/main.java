import java.util.Scanner;

class addition {
    void add(double a, double b) {
        System.out.println("Result: " + (a + b));
    }
}

class subtraction extends addition {
    void subtract(double a, double b) {
        System.out.println("Result: " + (a - b));
    }
}

class multiplication extends subtraction {
    void multiply(double a, double b) {
        System.out.println("Result: " + (a * b));
    }
}

class division extends multiplication {
    void divide(double a, double b) {
        if (b != 0) {
            System.out.println("Result: " + (a / b));
        } else {
            System.out.println("Error: Division by zero");
        }
    }
}

class main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        division calc = new division();

        System.out.println("Select operation: 1-Addition, 2-Subtraction, 3-Multiplication, 4-Division");
        int choice = scanner.nextInt();

        System.out.println("Enter first number:");
        double num1 = scanner.nextDouble();
        System.out.println("Enter second number:");
        double num2 = scanner.nextDouble();

        switch (choice) {
            case 1:
                calc.add(num1, num2);
                break;
            case 2:
                calc.subtract(num1, num2);
                break;
            case 3:
                calc.multiply(num1, num2);
                break;
            case 4:
                calc.divide(num1, num2);
                break;
            default:
                System.out.println("Invalid choice");
        }
        scanner.close();
    }
}