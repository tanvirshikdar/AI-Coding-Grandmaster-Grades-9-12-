class Hillstations {
    void location() {
        System.out.println("Location is:");
    }

    void famousfor() {
        System.out.println("Famous for:");
    }
}

class Manali extends Hillstations {
    @Override
    void location() {
        System.out.println("Manali is in Himachal Pradesh");
    }

    @Override
    void famousfor() {
        System.out.println("It is Famous for Hadimba Temple and adventure sports");
    }
}

class Mussoorie extends Hillstations {
    @Override
    void location() {
        System.out.println("Mussoorie is in Uttarakhand");
    }

    @Override
    void famousfor() {
        System.out.println("It is Famous for education institutions");
    }
}

class Gulmarg extends Hillstations {
    @Override
    void location() {
        System.out.println("Gulmarg is in J&K");
    }

    @Override
    void famousfor() {
        System.out.println("It is Famous for skiing");
    }
}

class Main {
    public static void main(String[] args) {
        Hillstations a = new Hillstations();
        Hillstations m = new Manali();
        Hillstations mu = new Mussoorie();
        Hillstations g = new Gulmarg();

        a.location();
        a.famousfor();

        m.location();
        m.famousfor();

        mu.location();
        mu.famousfor();

        g.location();
        g.famousfor();
    }
}