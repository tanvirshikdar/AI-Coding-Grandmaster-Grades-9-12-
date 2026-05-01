class superclass {
    int number = 56;
}

class subclass extends superclass {
    int number = 96;

    void printNumber() {
        System.out.println(number);
    }
}

class main {
    public static void main(String args[]) {
        subclass sub = new subclass();
        sub.printNumber();
    }
}