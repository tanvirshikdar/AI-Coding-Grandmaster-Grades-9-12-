class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        return f"Square(side={self.width})"


def main():
    print("--- Polygon Area Calculator ---")

    rect = Rectangle(10, 5)
    print(rect)
    print(f"Rectangle Area: {rect.get_area()}")

    print("-" * 30)

    sq = Square(4)
    print(sq)
    print(f"Square Area: {sq.get_area()}")

    print("\nUpdating square side to 7...")
    sq.set_side(7)
    print(sq)
    print(f"New Square Area: {sq.get_area()}")


if __name__ == "__main__":
    main()