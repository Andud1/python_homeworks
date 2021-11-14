#№5

i = 0
rubles = 0
pennies = 0
rubles1 = 0
pennies1 = 0
price_list_str = ""
price_list = [51.2, 53.23, 69, 1.2, 45.67, 11, 88.31, 99.99, 100, 321.32, 24.4, 82, 62.21, 132, 213]
for price in price_list:


    rubles1 = int(price // 1)
    pennies1 = int((price - rubles1) * 100)
    rubles1 = str(rubles1)
    pennies1 = str(pennies1).zfill(2)
    price_list_str += rubles1 + ' руб ' + pennies1 + ' коп, '



price_list.sort()

while i < len(price_list):

    rubles = int(price_list[i] // 1)
    pennies = int((price_list[i] - rubles) * 100)
    rubles = str(rubles)
    pennies = str(pennies).zfill(2)
    price_list[i] = rubles + ' руб ' + pennies + ' коп, '
    i += 1

price_list_2 = list(reversed(price_list))


print(price_list_str)

print(price_list)

print(price_list_2)
price_list_2 = price_list_2[:5]
price_list_2.reverse()
print(price_list_2)