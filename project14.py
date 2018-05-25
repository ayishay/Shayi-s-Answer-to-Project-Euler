def next_num(num):
    if num % 2:
        return 3 * num + 1
    else:
        return num / 2

def lengh_of_sequence(num):
    chain = [num]
    while num > 1:
        num = next_num(num)
        chain.append(num)
    return len(chain)

start_num = 0
max_start_num = 0
max_length = 0
while start_num < 1000000:
    start_num += 1
    new_length = lengh_of_sequence(start_num)
    if new_length > max_length:
        max_start_num = start_num
        max_length = new_length

print("start num ", max_start_num, " max_length ", max_length)





