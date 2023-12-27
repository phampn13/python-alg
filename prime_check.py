import math

def is_prime(number):
    if number < 2:
        return False
    
    sqrt_number = math.sqrt(number)

    # Cast sqrt_number to integer

    for num in range(2, int(sqrt_number) + 1):

        # If the number is divisible by a number other than 1 or itself,
        # the number is NOT prime.
        
        if number % num == 0:
            return False
    
    return True

num = 2
result = is_prime(num)

print(f'{num} is {"a prime number" if result else "not a prime number"}.')
