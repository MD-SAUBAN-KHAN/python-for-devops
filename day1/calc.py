import sys

"""Input validation to ensure we have the right number of arguments
following is the list of argv here ::
sys.argv[0] is the name of the script (e.g., calc.py).
sys.argv[1] is expected to be the first number.
sys.argv[2] is expected to be the operation (e.g., +, -, *, /).
sys.argv[3] is expected to be the second number."""

if len(sys.argv) != 4:
    print("Usage: python calc.py <num1> <operation> <num2>")
    sys.exit(1)

try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[3])
except ValueError:
    print("Error: Please provide valid numbers for num1 and num2.")
    sys.exit(1)

operation = sys.argv[2]

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 == 0:
        return "Error! Division by zero."
    return num1 / num2

if operation == "add" or operation == "+":
    print("===Addition of NUM1 & NUM2 is --->  " + str(add(num1, num2)))
elif operation == "sub" or operation == "-":
    print("===Substraction of NUM1 & NUM2 is --->  "+str(sub(num1, num2)))
elif operation == "mul" or operation == "*":
    print("===Multiplication of NUM1 & NUM2 is --->  "+str(mul(num1, num2)))
elif operation == "div" or operation == "/":
    print("===Division of NUM1 & NUM2 is --->  "+ str(div(num1, num2)))
else:
    print("Invalid operation. Use [add or +], [sub or -], [mul or *], [div or /]")
