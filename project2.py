def is_even(num):
    return num % 2 == 0

def sum_of_even(num):
    sum = 2
    pre1=1
    pre2=2
    fibnum = pre1 + pre2
    while(fibnum <= num):
        if is_even(fibnum):
            sum += fibnum
        pre1 = pre2
        pre2 = fibnum
        fibnum = pre1 + pre2
    return sum

print(sum_of_even(4000000))