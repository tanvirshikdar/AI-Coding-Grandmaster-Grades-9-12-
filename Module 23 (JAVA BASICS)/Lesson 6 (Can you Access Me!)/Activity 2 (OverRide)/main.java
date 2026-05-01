class parent {
    public void sayHello() {
        System.out.println("Hello from Parent");
    }
}

class child extends parent {
    @Override
    public void sayHello() {
        System.out.println("Hello from Child");
    }
}

class main {
    public static void main(String[] args) {
        parent p = new child();
        p.sayHello();
    }
}