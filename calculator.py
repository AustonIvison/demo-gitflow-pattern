class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def modulus(self, a, b):
        return a % b

    def square_root(self, a):
        return a ** 0.5

if __name__ == "__main__":
    calc = Calculator()
    print("1 + 2 =", calc.add(1, 2))
