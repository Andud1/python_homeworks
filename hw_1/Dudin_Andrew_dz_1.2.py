numbers = list(range(1, 1000, 2))
counter_1 = 0
counter_2 = 0
counter_3 = 0
temp_num = 0

for num in numbers:
    num = num ** 3
    temp_num = num
    counter_2 = 0
    while num > 0:
        counter_3 = num % 10
        num = num // 10
        counter_2 += counter_3
    if counter_2 % 7 == 0:
        counter_1 += temp_num


print(counter_1)
print(numbers)
counter_1 = 0


for num in numbers:
    num = num ** 3
    num += 17
    temp_num = num
    counter_2 = 0
    while num > 0:
        counter_3 = num % 10
        num = num // 10
        counter_2 += counter_3
    if counter_2 % 7 == 0:
        counter_1 += temp_num

print(counter_1)