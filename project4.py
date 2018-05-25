def is_palindrome(num):
    return str(num) == ''.join(reversed(str(num)))

def is_palindrome2(num):
    s = str(num)
    return s == s[::-1]

big = 100 * 100
for i in range(100,1000):
    for j in range(100,1000):
        if is_palindrome(i*j):
            big = max(big,i*j)

print(big)



    
