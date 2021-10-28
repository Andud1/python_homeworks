#№4
i = 0
i_2 = 0
arr = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
while i < len(arr):

    arr[i] = arr[i].split()[len(arr[i].split()) - 1]
    arr[i] = arr[i].capitalize()
    i += 1

while i_2 < len(arr):

    print('Привет,' + arr[i_2] + '!')
    i_2 += 1



print(arr)

