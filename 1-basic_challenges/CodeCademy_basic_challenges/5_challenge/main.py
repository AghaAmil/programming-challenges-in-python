def comparison_func(string):
    string = string.lower()
    x_counter = 0
    o_counter = 0

    for char in string:
        if char == 'x':
            x_counter += 1

        if char == 'o':
            o_counter += 1

    if x_counter == o_counter:
        return True, x_counter, o_counter
    else:
        return False, x_counter, o_counter

# using python build-in function
def comparison_func2(string):
    string = string.lower()

    x_counter = string.count('x')
    o_counter = string.count('o')

    if x_counter == o_counter:
        return True, x_counter, o_counter
    else:
        return False, x_counter, o_counter


user_input = input('Write a sentence: ')

result, Xs, Os = comparison_func(user_input)
# result, Xs, Os = comparison_func2(user_input)

print(f'The number of Xs in your sentence is: {Xs}')
print(f'The number of Os in your sentence is: {Os}')

if result:
    print('The number of Xs and Os in your sentence are equal.')
else:
    print('The number of Xs and Os in your sentence are not equal.')
