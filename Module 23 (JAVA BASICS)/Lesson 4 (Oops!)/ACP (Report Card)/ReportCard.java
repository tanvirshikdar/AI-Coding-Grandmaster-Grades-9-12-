class ReportCard {
    public static void main(String[] args) {
        String studentName = "Alexander";
        String studentClass = "10th Grade";
        
        int english = 85;
        int mathematics = 92;
        int socialScience = 78;
        int chemistry = 88;
        int physics = 84;
        int biology = 90;

        int totalMarks = english + mathematics + socialScience + chemistry + physics + biology;
        double percentage = (totalMarks / 600.0) * 100;

        System.out.println("REPORT CARD");
        System.out.println("Name: " + studentName);
        System.out.println("Class: " + studentClass);
        System.out.println("---------------------------");
        System.out.println("English: " + english);
        System.out.println("Mathematics: " + mathematics);
        System.out.println("Social Science: " + socialScience);
        System.out.println("Chemistry: " + chemistry);
        System.out.println("Physics: " + physics);
        System.out.println("Biology: " + biology);
        System.out.println("---------------------------");
        System.out.println("Total Marks: " + totalMarks);
        System.out.println("Percentage: " + percentage + "%");
    }
}