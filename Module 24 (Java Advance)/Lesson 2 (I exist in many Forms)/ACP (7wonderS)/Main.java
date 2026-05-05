class SevenWonders {
    public void displayLocation() {
        System.out.println("The location of this wonder is:");
    }
}

class TajMahal extends SevenWonders {
    @Override
    public void displayLocation() {
        System.out.println("Taj Mahal is located in Agra, India.");
    }
}

class GreatWallOfChina extends SevenWonders {
    @Override
    public void displayLocation() {
        System.out.println("The Great Wall is located in China.");
    }
}

class Petra extends SevenWonders {
    @Override
    public void displayLocation() {
        System.out.println("Petra is located in Ma'an, Jordan.");
    }
}

class Colosseum extends SevenWonders {
    @Override
    public void displayLocation() {
        System.out.println("The Colosseum is located in Rome, Italy.");
    }
}

class ChichenItza extends SevenWonders {
    @Override
    public void displayLocation() {
        System.out.println("Chichen Itza is located in Yucatan, Mexico.");
    }
}

class MachuPicchu extends SevenWonders {
    @Override
    public void displayLocation() {
        System.out.println("Machu Picchu is located in Cuzco Region, Peru.");
    }
}

class ChristTheRedeemer extends SevenWonders {
    @Override
    public void displayLocation() {
        System.out.println("Christ the Redeemer is located in Rio de Janeiro, Brazil.");
    }
}

class Main {
    public static void main(String[] args) {
        SevenWonders[] wonders = {
            new TajMahal(),
            new GreatWallOfChina(),
            new Petra(),
            new Colosseum(),
            new ChichenItza(),
            new MachuPicchu(),
            new ChristTheRedeemer()
        };

        for (SevenWonders wonder : wonders) {
            wonder.displayLocation();
        }
    }
}