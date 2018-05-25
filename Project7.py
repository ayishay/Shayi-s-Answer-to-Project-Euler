def is_prime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

index = 1
number = 2
while (index != 10001):
    number += 1
    if is_prime(number):
        index += 1
print(number)

