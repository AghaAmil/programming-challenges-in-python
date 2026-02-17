def vowels_counter(sentence):
    sentence = sentence.lower()

    vowels_counter = 0
    vowels_counter_a = 0
    vowels_counter_e = 0
    vowels_counter_i = 0
    vowels_counter_o = 0
    vowels_counter_u = 0

    vowels_list = []

    for char in sentence:
        if char in 'aeiou':
            vowels_counter += 1
            vowels_list.append(char)

            if char == 'a':
                vowels_counter_a += 1
            elif char == 'e':
                vowels_counter_e += 1
            elif char == 'i':
                vowels_counter_i += 1
            elif char == 'o':
                vowels_counter_o += 1
            elif char == 'u':
                vowels_counter_u += 1

    return vowels_list,vowels_counter, vowels_counter_a, vowels_counter_e, vowels_counter_i, vowels_counter_o, vowels_counter_u


user_input = input('Enter a sentence in order to count its vowels: ')

vowels_list, vowels_counter, vowels_counter_a, vowels_counter_e, vowels_counter_i, vowels_counter_o, vowels_counter_u = vowels_counter(
    user_input)

print()

print('The list of vowels in your sentence', vowels_list)
print(f'The number of "a" vowel in your sentence: {vowels_counter_a}')
print(f'The number of "e" vowel in your sentence: {vowels_counter_e}')
print(f'The number of "i" vowel in your sentence: {vowels_counter_i}')
print(f'The number of "o" vowel in your sentence: {vowels_counter_o}')
print(f'The number of "u" vowel in your sentence: {vowels_counter_u}')
print('The number of vowels in your sentence', vowels_counter)
