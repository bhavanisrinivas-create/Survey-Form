class Calculator:
    def  __init__(self, a: float, b: float, operation: str):
      self.a = a
      self.b = b
      self.operation = operation.lower()

    def calculator(self):
        if self.operation in ["add", "addition"]:
            return self.a + self.b
        elif self.operation in ["sub", "subtraction"]:
             return self.a - self.b
        elif self.operation in ["mul", "multiplication"]:
             return self.a * self.b
        elif self.operation in ["div", "division"]:
          if self.b !=0:
            return self.a  / self.b
          else:
            return "Error : Division by zero is not allowed."
        else:
            return "Invalid operation. Use add, sub, mul, div."        
  


if __name__ == "__main__":
    try:
        a = float(input("Enter first number (a) :"))
        b = float(input("Enter first number (b) :"))
        operation = input("Enter operation (add, sub, mul, div):")

        calc = Calculator(a, b, operation)
        result  = calc.calculator()
        print(f"Result: {result}")
    except ValueError:
        print("Error : Please enter valid numbers.")
