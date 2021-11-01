#№2
n = int(input('f'))
num_gen = (num for num in range(1, n+1, 2))



#№3
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Андрей'
]
klasses = [
     '9А', '7В', '9Б', '9В', '8Б', '10А'
 ]

def gen_tuples():
    i = 0

    while i < len(tutors):
        if i > len(klasses) - 1:
            yield(tutors[i], None)

        else:
            yield(tutors[i], klasses[i])
        i += 1


#№4
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result1 = []
i3 = 0
while i3 < len(src):
   if i3 != 0:
       if src[i3] > src[i3 - 1]:
            result1.append(src[i3])
   i3 += 1

print(result1)

#5
src2 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
tmp = set()
unique_numbers = set()
for num in src2:
    if num not in tmp:
        unique_numbers.add(num)
    else:
        unique_numbers.discard(num)
    tmp.add(num)
correct_dir_unique_numbers = [num for num in src2 if num in unique_numbers]
print(correct_dir_unique_numbers)
