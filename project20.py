#Factorial digit sum
#Project Euler Problem 20 
#n! means n × (n − 1) × ... × 3 × 2 × 1

#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

#Find the sum of the digits in the number 100!
def factorial(num):
    result = num
    while num is not 1:
        num -= 1
        result *= num
    return result

def sum_of_digits(num):
    result = 0
    for i in str(num):
        result += int(i)
    return result
print(sum_of_digits(factorial(100)))