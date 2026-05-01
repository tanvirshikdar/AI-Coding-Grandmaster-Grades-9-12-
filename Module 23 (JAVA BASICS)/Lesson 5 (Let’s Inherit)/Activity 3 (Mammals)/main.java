class mammals {
    void mam() {
        System.out.println("Inside Mammals Class");
    }
}

class lion extends mammals {
    void roar() {
        System.out.println("Inside Lion class ");
    }
}

class human extends mammals {
    void hum() {
        System.out.println("Inside Human");
    }
}

class main {
    public static void main(String args[]) {
        lion obj = new lion();
        obj.roar();
        obj.mam();

        human obj2 = new human();
        obj2.hum();
    }
}