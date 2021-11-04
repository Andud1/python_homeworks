import sys

if len(sys.argv) != 2:
    print('Error! 1 argument expected.')
else:
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(str(sys.argv[1]) + '\n')