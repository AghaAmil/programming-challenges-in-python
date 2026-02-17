# Solving based on mathematics solution from https://www.cuemath.com/numbers/prime-numbers/

def prime_detector(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


print('The program generates prime numbers up to a given limit.')
limit_number = int(input('Enter the limit: '))

primes_list = []

for num in range(2, limit_number + 1):
    if prime_detector(num):
        primes_list.append(num)

print(f'The list of prime numbers up to {limit_number} is: {primes_list}')
