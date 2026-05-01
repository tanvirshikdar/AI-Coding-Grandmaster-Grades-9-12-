class counter {
    int number = 10;

    void increment() {
        number = number + 1;
    }

    public static void main(String[] args) {
        counter obj1 = new counter();
        counter obj2 = new counter();
        counter obj3 = new counter();

        obj1.increment();
        obj2.increment();
        obj3.increment();

        System.out.println(obj1.number);
        System.out.println(obj2.number);
        System.out.println(obj3.number);
    }
}