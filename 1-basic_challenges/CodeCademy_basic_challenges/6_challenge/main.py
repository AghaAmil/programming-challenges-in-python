def calculator(num1, num2, operator):
    try:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")


def num_input(user_input):
    while True:
        try:
            # the input number will be changed to float number. therefore 7 shows as 7.0
            number = float(input(user_input))

            # below condition will return integers in integers format instead of float illustration
            # display 7 instead of 7.0
            if number.is_integer():
                return int(number)

            return number

        except ValueError:
            print('Invalid input. Enter a numerical number')


def operator_input(user_input):
    while True:
        operator = input(user_input)
        if operator not in ['+', '-', '*', '/']:
            print('Invalid operator. Choose a valid operator out of (+, -, /, or *): ')
        else:
            return operator


print('The program below is a simple calculator.')

first_number = num_input('Enter the first number: ')
operation = operator_input('Select the mathematical operator: (+, -, /, or *): ')
second_number = num_input('Enter the second number: ')

result = calculator(first_number, second_number, operation)

print()
print(f'{first_number} {operation} {second_number} = {result}')
