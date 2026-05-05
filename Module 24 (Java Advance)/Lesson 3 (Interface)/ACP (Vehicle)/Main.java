import java.util.Scanner;

interface Vehicle {
    void changeGear(int a);
    void speedUp(int a);
    void applyBrakes(int a);
    void printStates();
}

class Truck implements Vehicle {
    private int speed;
    private int gear;

    @Override
    public void changeGear(int newGear) {
        gear = newGear;
    }

    @Override
    public void speedUp(int increment) {
        speed += increment;
    }

    @Override
    public void applyBrakes(int decrement) {
        speed -= decrement;
    }

    @Override
    public void printStates() {
        System.out.println("Truck Speed: " + speed + " | Gear: " + gear);
    }
}

class Bike implements Vehicle {
    private int speed;
    private int gear;

    @Override
    public void changeGear(int newGear) {
        gear = newGear;
    }

    @Override
    public void speedUp(int increment) {
        speed += increment;
    }

    @Override
    public void applyBrakes(int decrement) {
        speed -= decrement;
    }

    @Override
    public void printStates() {
        System.out.println("Bike Speed: " + speed + " | Gear: " + gear);
    }
}

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Vehicle truck = new Truck();
        Vehicle bike = new Bike();

        System.out.print("Enter Truck gear: ");
        truck.changeGear(scanner.nextInt());
        System.out.print("Enter Truck speed increment: ");
        truck.speedUp(scanner.nextInt());
        System.out.print("Enter Truck brake decrement: ");
        truck.applyBrakes(scanner.nextInt());

        System.out.print("Enter Bike gear: ");
        bike.changeGear(scanner.nextInt());
        System.out.print("Enter Bike speed increment: ");
        bike.speedUp(scanner.nextInt());
        System.out.print("Enter Bike brake decrement: ");
        bike.applyBrakes(scanner.nextInt());

        truck.printStates();
        bike.printStates();
        
        scanner.close();
    }
}