from code_completion import add

# define a calculator class with a member function 'addition' which wraps the add function from code_completion.py
class Calculator:
    def addition(self, a, b):
        return add(a, b)

# call the adddition method of the calculator class and print the result
calculator = Calculator()
result = calculator.addition(1, 2)
print(result)
