import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    # Square Root Function
    def square_root(self, x):
        if x < 0:
            raise ValueError("Cannot calculate the square root of a negative number.")
        return math.sqrt(x)

if __name__ == "__main__":
    calculator = Calculator()
    
    num1 = 16
    num2 = 4

    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")

    # Testing Square Root Function
    num3 = 25
    print(f"The square root of {num3} = {calculator.square_root(num3)}")

    # Handling negative square root case
    try:
        num4 = -9
        print(f"The square root of {num4} = {calculator.square_root(num4)}")
    except ValueError as e:
        print(e)
