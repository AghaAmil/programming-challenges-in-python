import os

from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 - n2


def calculation(operation_symbol, first_number, second_number):
    """
    the calculation function

    :param operation_symbol: string
    :param first_number: float
    :param second_number: float
    :return: float: return the calculated result by on selected operation
    """
    # the operators are stored as keys of a dictionary, the value of each operator is a function
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

    result = operations[operation_symbol](first_number, second_number)

    return result


def calculator_program():
    """
    the calculator program and main operation
    """
    print(logo)
    first_number = float(input("what's the first number?: "))

    # continue or not
    while True:
        print("+\n-\n*\n/")
        operation_symbol = input("Pick an operation: ")
        second_number = float(input("what's the next number?: "))
        calculation_result = calculation(operation_symbol, first_number, second_number)
        print(f"{first_number} {operation_symbol} {second_number} = {calculation_result}")

        continue_operation = input(
            f"Type 'y' to continue calculating with {calculation_result} or type 'n' to start a new calculation: "
        )

        if continue_operation == "y":
            first_number = calculation_result
        else:
            break

    # clear terminal viewpoint
    os.system("cls" if os.name == "nt" else "clear")
    # run the program again from the start
    calculator_program()


# run the program
calculator_program()
