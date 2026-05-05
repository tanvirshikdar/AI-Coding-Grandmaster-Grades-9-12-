class Shape {
    public double getVolume() {
        return 0;
    }
}

class Cube extends Shape {
    private double side;

    public Cube(double side) {
        this.side = side;
    }

    @Override
    public double getVolume() {
        return Math.pow(side, 3);
    }
}

class Cuboid extends Shape {
    private double length;
    private double width;
    private double height;

    public Cuboid(double length, double width, double height) {
        this.length = length;
        this.width = width;
        this.height = height;
    }

    @Override
    public double getVolume() {
        return length * width * height;
    }
}

class Cylinder extends Shape {
    private double radius;
    private double height;

    public Cylinder(double radius, double height) {
        this.radius = radius;
        this.height = height;
    }

    @Override
    public double getVolume() {
        return Math.PI * Math.pow(radius, 2) * height;
    }
}

class Main {
    public static void main(String[] args) {
        Shape cube = new Cube(5);
        Shape cuboid = new Cuboid(4, 5, 6);
        Shape cylinder = new Cylinder(3, 7);

        System.out.println("Volume of Cube: " + cube.getVolume());
        System.out.println("Volume of Cuboid: " + cuboid.getVolume());
        System.out.println("Volume of Cylinder: " + cylinder.getVolume());
    }
}