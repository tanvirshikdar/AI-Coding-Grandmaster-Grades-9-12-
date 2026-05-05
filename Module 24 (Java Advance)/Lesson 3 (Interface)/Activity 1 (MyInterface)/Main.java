interface MyInterface {
    void method1();

    void method2();
}

class Main implements MyInterface {
    @Override
    public void method1() {
        System.out.println("implementation of method1");
    }

    @Override
    public void method2() {
        System.out.println("implementation of method2");
    }

    public static void main(String[] args) {
        MyInterface obj = new Main();
        obj.method1();
        obj.method2();
    }
}