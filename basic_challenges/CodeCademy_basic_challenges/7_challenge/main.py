def doubler(string):
    char_list = []

    for char in string:
        char_list.append(char * 2)

    return ''.join(char_list)


input_string = input('Enter a word, sentence or a string: ')

print(doubler(input_string))