abstract class Objects {
    abstract void showShape();

    public void shape() {
        System.out.println("I'm form abstract class");
    }
}

class Sphere extends Objects {
    @Override
    void showShape() {
        System.out.println("Object type is Sphere.");
    }
}

class Cuboid extends Objects {
    @Override
    void showShape() {
        System.out.println("Object type is Cuboid.");
    }
}

class Prism extends Objects {
    @Override
    void showShape() {
        System.out.println("Object type is Prism.");
    }
}

public class Main {
    public static void main(String[] args) {
        Objects obj = new Sphere();
        obj.showShape();

        obj = new Cuboid();
        obj.showShape();

        obj = new Prism();
        obj.showShape();

        obj.shape();
    }
}