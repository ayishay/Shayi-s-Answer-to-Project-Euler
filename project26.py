#project Euler problem 26
#A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

#1/2	= 	0.5
#1/3	= 	0.(3)
#1/4	= 	0.25
#1/5	= 	0.2
#1/6	= 	0.1(6)
#1/7	= 	0.(142857)
#1/8	= 	0.125
##1/9	= 	0.(1)
#1/10	= 	0.1
#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def is_prime(num):
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i+=1           
    return True

def prime_list_below(num):
    l = []
    for i in range(2,num+1):
        if (is_prime(i)):
            l.append(i)
    return l

max_num = 0
max_recurring = 0
for i in prime_list_below(1000):
     for j in range(1,1000):
        if 10**j%i == 1:
            if j > max_recurring:
                max_recurring = j
                max_num = i
            break
print(i)




