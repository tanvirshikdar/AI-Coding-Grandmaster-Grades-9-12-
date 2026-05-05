import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] accountNames = new String[1000];
        double[] accountBalances = new double[1000];
        int size = 100;
        boolean isRunning = true;

        while (isRunning) {
            try {
                System.out.println("Welcome to Codingal Banking Services");
                System.out.println("1. Add Customer");
                System.out.println("2. Summary of All Accounts");
                System.out.println("3. Quit");
                System.out.print("Select an option: ");

                int option = scanner.nextInt();

                if (option < 1 || option > 3) {
                    throw new InvalidOptionException("Invalid Menu Option selected: " + option);
                }

                if (option == 1) {
                    scanner.nextLine();
                    System.out.print("Enter Name: ");
                    String name = scanner.nextLine();

                    System.out.print("Enter Opening Balance: ");
                    double balance = scanner.nextDouble();

                    if (balance < 500) {
                        throw new InsufficientBalanceException("Opening balance must be at least 500 Rs.");
                    }

                    accountNames[size] = name;
                    accountBalances[size] = balance;
                    System.out.println("Account created. Account Number: " + size);
                    size++;

                } else if (option == 2) {
                    System.out.println("--- Account Summary ---");
                    for (int i = 100; i < size; i++) {
                        System.out.println("ID: " + i + " | Name: " + accountNames[i] + " | Balance: " + accountBalances[i]);
                    }

                } else if (option == 3) {
                    isRunning = false;
                    System.out.println("Thank you for using Codingal Banking Services.");
                }

            } catch (InvalidOptionException | InsufficientBalanceException e) {
                System.out.println("Error: " + e.getMessage());
            } catch (Exception e) {
                System.out.println("An unexpected error occurred. Please try again.");
                scanner.nextLine();
            }
            System.out.println("================================");
        }
        scanner.close();
    }
}