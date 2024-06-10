from code_completion import add

# define a calculator class which uses the add function from 00_code_completion.py
class Calculator:
    def addition(self, a, b):
        return add(a, b)

# call the add method of the calculator class
calculator = Calculator()
result = calculator.addition(1, 2)
print(result)
