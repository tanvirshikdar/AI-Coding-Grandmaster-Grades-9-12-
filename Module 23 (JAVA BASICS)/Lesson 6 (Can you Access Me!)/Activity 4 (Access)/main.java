class parent {
    protected void protect() {
        System.out.println("I'm inside protected method");
    }
}

class child extends parent {
    private void privateMethod() {
        System.out.println("I'm inside private method");
    }
}

class main {
    public static void main(String[] args) {
        child kid = new child();
        System.out.println("Hello world!");
    }
}