import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<String> names = new ArrayList<>();

        System.out.println("How many names would you like to enter?");
        int count = scanner.nextInt();
        scanner.nextLine();

        for (int i = 0; i < count; i++) {
            System.out.println("Enter name " + (i + 1) + ":");
            names.add(scanner.nextLine());
        }

        System.out.println("Enter the name you want to search for:");
        String targetName = scanner.nextLine();

        names.forEach(name -> {
            if (name.equalsIgnoreCase(targetName)) {
                System.out.println("Eureka");
            }
        });

        scanner.close();
    }
}