import math

def radian_to_degree(radian):
    return radian * 180 / math.pi

# error and exception handling
while True:
    try:
        degree_in_radian = float(input('Enter a angle in Radian: '))

        # Format to 3 decimal places
        print(f'The entered angle in degree is: {radian_to_degree(degree_in_radian):.3f}')
        break

    except ValueError:
        print('Please enter a numeric number.')
        print()

