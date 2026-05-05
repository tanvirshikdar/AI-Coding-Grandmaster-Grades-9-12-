import java.util.Scanner;

public class Main {
    public static Candidate getCandidateDetails() throws InvalidInternException {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the candidate Details");

        System.out.println("Name:");
        String name = scanner.next();

        System.out.println("Gender:");
        String gender = scanner.next();

        System.out.println("Enter Percentage in 10th:");
        int percentage = scanner.nextInt();

        if (percentage < 50) {
            throw new InvalidInternException("Registration Failed. Percentage cannot be less than 50%.");
        } else {
            Candidate candidate = new Candidate();
            candidate.setName(name);
            candidate.setGender(gender);
            candidate.setPercentage(percentage);

            return candidate;
        }
    }

    public static void main(String[] args) {
        System.out.println("Welcome to InterHiring Tool");

        try {
            Candidate candidate = getCandidateDetails();
            System.out.println("Registration Successful for: " + candidate.getName());
        } catch (InvalidInternException e) {
            System.out.println(e.getMessage());
        }
    }
}