import java.util.ArrayList;
import java.util.List;

class Main {
    public static void main(String[] args) {
        List<String> animals = new ArrayList<>();

        animals.add("Lion");
        animals.add("Tiger");
        animals.add("Cheetah");

        System.out.println("=============Printing Current Array==========");
        System.out.println(animals);

        animals.clear();

        System.out.println("=============Printing Cleared Array==========");
        System.out.println("Empty Array : " + animals);

        if (animals.isEmpty()) {
            System.out.println("Array is empty");
        } else {
            System.out.println("Array is not empty");
        }

        animals.add("Lion");
        animals.add("Tiger");
        animals.add("Cheetah");

        System.out.println("The size of Array: " + animals.size());
        System.out.println("Adding more element " + animals.add("Dog"));
        System.out.println(animals);

        animals.remove(2);
        System.out.println(animals);
    }
}