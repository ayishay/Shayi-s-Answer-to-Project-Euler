# Project Euler Problem #10 - Summation of Primes (in Python)
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# returns True if parameter n is a prime number, False if composite and "Neither prime, nor composite" if neither
def is_prime(num):
    for i in range(2, int(num**0.5) +1):
        if num % i == 0:
            return False
    return True

def sum_of_prime_below(num):
    sum = 0
    for i in range(2,num):
        if is_prime(i):
            sum += i
    return sum

print(sum_of_prime_below(2000000))