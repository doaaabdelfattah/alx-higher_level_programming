#!/usr/bin/python3
# Your code should not be executed when imported
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argcount = len(sys.argv)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    # Check arguments count
    if argcount != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operators = ['+', '-', '*', '/']
    op = sys.argv[2]

    # Check the operator
    if op not in operators:
        print("Unknown operator. Available operators: +, -, * and / ")
        exit(1)

    # Calculate
    if op == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif op == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif op == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif op == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
