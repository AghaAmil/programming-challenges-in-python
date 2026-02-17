# sorting using python built-in methods
def sorting(array, option):
    if option == 'asc':
        return sorted(array)
    elif option == 'desc':
        return sorted(array, reverse=True)
    else:
        return array


# sorting using bubble sort
def bubble_sort(array, option):
    option = option.lower()

    def asc(array):
        for i in range(len(array)):
            for j in range(len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]

        return array

    def desc(array):
        for i in range(len(array)):
            for j in range(len(array) - i - 1):
                if array[j] < array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]

        return array

    if option == 'asc':
        return asc(array)
    elif option == 'desc':
        return desc(array)
    else:
        return array


input_numbers = input('Enter the list of numbers (The numbers should be separated by space): ')
input_sort = input('Enter the sorting options out of (asc,desc,none): ')

input_numbers = [int(num) for num in input_numbers.split(' ')]

print(f'The sorted list based on {input_sort} is: {bubble_sort(input_numbers, input_sort)}')
print(f'The sorted list based on {input_sort} is: {sorting(input_numbers, input_sort)}')
