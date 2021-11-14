
#№1
a = 15 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 3

print(type(a))
print(type(b))
print(type(c))
print(type(d))


#№3
i = 0
i_2 = 0
logic_1 = False
arr = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

while i < len(arr):
    logic_2 = False
    logic_1 = False
    if arr[i][0] == '+' or arr[i][0] == '-':
        temp_sign = arr[i][1:]
        temp_sign2 = arr[i][0]

        if temp_sign.isdigit():
            logic_1 = True
            logic_2 = True



    elif arr[i].isdigit():
        temp_sign = arr[i]
        logic_1 = True

    if logic_1 == True:
        if logic_2 == False:
            arr[i] = arr[i].zfill(2)
        else:
            arr[i] = temp_sign.zfill(2)
            arr[i] = temp_sign2 + arr[i]



        arr.insert(i, '"')
        i += 2
        arr.insert(i, '"')



    i += 1

elements = ''
counter_1 = 0

while i_2 < len(arr):
    if arr[i_2] == '"':
        counter_1 += 1
        if counter_1 % 2 == 0:
            elements += arr[i_2] + ' '

        else:
            elements += arr[i_2]

    elif arr[i_2] != '"' and counter_1 % 2 != 0:
        elements += arr[i_2]


    else:
        elements += arr[i_2] + ' '
    i_2 += 1

print(arr)
print(elements)
