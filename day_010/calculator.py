import os
import art


def clear():
    # for Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for Unix
    else:
        _ = os.system('clear')


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        print("Can't divide by zero!")
        return None

    return a / b


def calculator():
    clear()
    print(art.logo)

    x = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:

        operation_symbol = input("Pick the operation: ")

        y = float(input("What's the next number?"))

        if operation_symbol in operations:
            result = operations[operation_symbol](x, y)
            result = round(result, 3)
            print(x, operation_symbol, y, "=", result)
        else:
            print("Wrong operation!")
            continue

        should_continue = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if should_continue == "y":
            x = result
        else:
            should_continue = False
            calculator()


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

calculator()