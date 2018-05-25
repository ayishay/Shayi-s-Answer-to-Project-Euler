#Power digit sum
#Project Euler Problem 16 
#215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 21000?

def sum_of_digits(num):
    result = 0
    for s in str(num):
        result += int(s)
    return result

print(sum_of_digits(2**1000))