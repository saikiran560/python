class PowerCalculator:
    @staticmethod
    def pow(x, n):
        return x ** n

# Example usage:
if __name__ == "__main__":
    calculator = PowerCalculator()

    
    base = int(input("Enter the base (x): "))
    exponent = int(input("Enter the exponent (n): "))

    result = calculator.pow(base, exponent)
    print(f"{base}^{exponent} is: {result}")
