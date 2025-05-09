#Welcome to Calculator
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2


operations={}
operations["+"]=add
operations["-"]=subtract
operations["*"]=multiply
operations["/"]=divide



def calculator():
    print("Welcome to the calculator")
    num1=float(input("Enter first number: "))
    for symbol in operations:
        print(symbol)
    should_continue=True
    while should_continue:
        operation_symbol=input("Pick an operation from the line above: ")
        num2=float(input("Enter next number: "))
        calculation_function=operations[operation_symbol]
        answer=calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")=="y":
            num1=answer
        else:
            should_continue=False
            calculator()
calculator()

# This code is a simple calculator that performs basic arithmetic operations (addition, subtraction, multiplication, and division).