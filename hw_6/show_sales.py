import sys

with open('bakery.csv', 'r', encoding='utf_8') as f:
    if len(sys.argv) == 1:
        print(f.read())
    elif len(sys.argv) == 2:
        content = f.read().splitlines()
        content = content[int(sys.argv[1])-1:]
        content_str = '\n'.join(content)
        print(content_str)
    elif len(sys.argv) == 3:
        content = f.read().splitlines()
        content = content[int(sys.argv[1]) - 1:int(sys.argv[2])]
        content_str = '\n'.join(content)
        print(content_str)

    else:
        print('Error! Wrong number of arguments.')