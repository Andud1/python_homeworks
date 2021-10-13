numbers = list(range(1, 101))
print(numbers)
words_list =['процент', 'процента', 'процентов']
for num in numbers:
    if num < 10:
        if num == 1:
            print(num, words_list[0])

        elif num > 1 and num < 5:
            print(num, words_list[1])

        else:
            print(num, words_list[2])

    elif num > 10 and num < 20:
        print(num, words_list[2])

    else:
        if num % 10 == 1:
            print(num, words_list[0])

        elif num % 10 > 1 and num % 10 < 5:
            print(num, words_list[1])

        else:
            print(num, words_list[2])


