import math

class ShapeCalculator:
    def area(self, arg1=0, arg2=0):
        if arg1 > 0 and arg2 == 0:
            return math.pi * arg1**2
        elif arg1 > 0 and arg2 > 0:
            return arg1 * arg2
        else:
            return "Invalid input. Please provide valid dimensions."

if __name__ == "__main__":
    calculator = ShapeCalculator()
    circle_area = calculator.area(5)
    print(f"Area of the circle: {circle_area:.2f}")
    rectangle_area = calculator.area(4, 6)
    print(f"Area of the rectangle: {rectangle_area}")
    invalid_area = calculator.area()
    print(f"Invalid case: {invalid_area}")