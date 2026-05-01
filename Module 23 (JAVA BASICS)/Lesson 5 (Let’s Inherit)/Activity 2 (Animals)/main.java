class animal {
    void eat() {
        System.out.println("eating...Animal class...eat method");
    }
}

class lion extends animal {
    void roar() {
        System.out.println("Roar...Lion class...roar method");
    }
}

class BabyLion extends lion {
    void weep() {
        System.out.println("weeping...BabyLion class...weep method");
    }
}

class main {
    public static void main(String args[]) {
        BabyLion obj = new BabyLion();
        obj.weep();
        obj.roar();
        obj.eat();
    }
}