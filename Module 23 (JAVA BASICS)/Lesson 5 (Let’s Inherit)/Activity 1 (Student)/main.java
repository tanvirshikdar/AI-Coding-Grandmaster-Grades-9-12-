class parent {
    int age, id;
    String name;

    void naming(String name) {
        System.out.println("Name: " + name);
    }
}

class child extends parent {
    void ageN(int age) {
        System.out.println("Age of student is: " + age);
    }
}

class main {
    public static void main(String[] er) {
        child s = new child();
        s.naming("Aashish");
        s.ageN(14);
    }
}