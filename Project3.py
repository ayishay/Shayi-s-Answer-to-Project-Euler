def larget_prime(num):
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else: num = num / i
    return num

print(larget_prime(600851475143))

