import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean isRunning = true;
        double[] accountBalances = new double[1000];
        String[] accountNames = new String[1000];
        int size = 100;

        while (isRunning) {
            System.out.println("Welcome to Codingal Banking Services");
            System.out.println("Banking Menu: ");
            System.out.println("Select any one option from below. ");
            System.out.println("1-> Add Customer");
            System.out.println("2-> Change Customer Name");
            System.out.println("3-> Check Account Balance");
            System.out.println("4-> Update Account Balance");
            System.out.println("5-> Summary of All Accounts");
            System.out.println("6-> Quit");
            System.out.print("Enter your option to proceed ahead: ");

            int option = scanner.nextInt();

            if (option == 1) {
                System.out.println("\nAdd Customer \nMenu->");
                scanner.nextLine();

                System.out.print("\nEnter Customer Name: ");
                String name = scanner.nextLine();
                accountNames[size] = name;

                System.out.print("Enter Opening Balance Amount: ");
                double amount = scanner.nextDouble();
                accountBalances[size] = amount;

                System.out.println("Account created successfully. \n");
                System.out.println("Account Details:- \n ");
                System.out.println("Account Number: " + size);
                System.out.println("Account Name: " + accountNames[size]);
                System.out.println("Account Balance: " + accountBalances[size] + " Rs \n");
                System.out.println("=================================");

                size++;

            } else if (option == 2) {
                System.out.println("\nChange Customer Name Menu");
                System.out.print("\nEnter your Account Number: ");

                int accountIndex = scanner.nextInt();
                scanner.nextLine();

                if (accountIndex >= size || accountIndex < 100) {
                    System.out.println("Account does not exist.");
                } else {
                    String oldName = accountNames[accountIndex];
                    System.out.print("Enter the new name: ");
                    String newName = scanner.nextLine();
                    accountNames[accountIndex] = newName;
                    System.out.println("Name is successfully updated from " + oldName + " to " + newName + ". \n");
                }
                System.out.println("=================================");

            } else if (option == 3) {
                System.out.println("\nCheck Account Balance Menu");
                System.out.print("\nEnter your Account Number: ");

                int accountIndex = scanner.nextInt();

                if (accountIndex >= size || accountIndex < 100) {
                    System.out.println("Account does not exist.");
                } else {
                    System.out.println(accountNames[accountIndex] + " your balance is " + accountBalances[accountIndex] + " Rs.");
                }
                System.out.println("=================================");

            } else if (option == 4) {
                System.out.println("\nUpdate Account Balance Menu ");
                System.out.print("\nEnter your Account Number: ");

                int accountIndex = scanner.nextInt();

                if (accountIndex >= size || accountIndex < 100) {
                    System.out.println("Account does not exist.");
                } else {
                    System.out.print("Enter the amount to be deposited: ");
                    double depositAmount = scanner.nextDouble();

                    accountBalances[accountIndex] += depositAmount;
                    System.out.println(accountNames[accountIndex] + " your updated balance is : " 
                        + accountBalances[accountIndex] + " Rs. \n ");
                }
                System.out.println("=================================");

            } else if (option == 5) {
                System.out.println("Accounts registered\n");

                for (int i = 100; i < size; i++) {
                    System.out.println("Account Number: " + i + ", Name: " + accountNames[i] + ", Balance: " 
                        + accountBalances[i] + " Rs. \n ");
                }
                System.out.println("=================================");

            } else if (option == 6) {
                System.out.println("Terminating...");
                System.out.println("Developed & Managed by Aashish@Codingal");
                System.out.println("Built with ❤ in India");
                isRunning = false;

            } else {
                System.out.println("\n Invalid input.");
                System.out.println("Terminating...");
                System.out.println("Developed & Managed by Aashish@Codingal");
                System.out.println("Built with ❤ in India");
                isRunning = false;
            }
        }
        scanner.close();
    }
}