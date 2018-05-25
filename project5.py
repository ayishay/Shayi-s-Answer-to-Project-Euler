def is_multiple(num):
    for i in range(1,21):
        if num % i:
            return False
    return

number = 1
while is_multiple(number) == False:
    number += 1

print(number)

            
