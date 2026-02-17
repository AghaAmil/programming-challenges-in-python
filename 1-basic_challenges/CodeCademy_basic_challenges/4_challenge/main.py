def ccn_encrypter_1(card_number):
    # convert to list as strings are immutable
    card_number = list(card_number)

    for index in range(len(card_number) - 4):
        card_number[index] = '*'

    return ''.join(card_number)

def ccn_encrypter_2(card_number):
    encrypted = card_number[:3] + ' **** **** ' + card_number[-4:]

    return encrypted

ccn = input('Enter Your Credit Card Number: ')

while len(ccn) != 16 or not ccn.isdigit():
    print('Invalid Credit Card Number entered')
    print()

    ccn = input('Enter Your Credit Card Number: ')

print(f'The Encrypted Credit Card Number is: {ccn_encrypter_1(ccn)}')
print(f'The Encrypted Credit Card Number is: {ccn_encrypter_2(ccn)}')