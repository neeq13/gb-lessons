def save():
    lastname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    patronomic = input('Введите отчество: ')
    phone = input('Введите телефон в формате (9183334455): ')
    with open('file.txt', 'a', encoding='utf-8') as data:
        print(lastname, name, patronomic, phone, file=data)

def search(str):
    with open('file.txt', 'r', encoding='utf-8') as data:
        if str == '':
            for i in data:
                print(i, end='')
            print('--------------')
        else:
            count = 0
            for line in data:
                for i in line.split():
                    if i in str:
                        count += 1
                if count == len(str):
                    print(line, end='')
                count = 0

def delete():
    str = input('Введите поисковый запрос для удаления, все слова должны быть раздеелны пробелами: ').lower().split()
    list = []
    count=0
    with open('file.txt', 'r', encoding='utf-8') as data:
        for line in data:
            for i in line.split():
                if i.lower() in str:
                    count += 1
            if count != len(str):
                if line != '':
                    list.append(line)
            count = 0
    with open('file.txt', 'w', encoding='utf-8') as data:
        if len(str) != 0:
            for line in list:
                print(line, file=data)

def update():
    str = input('Введите поисковый запрос для замены, все слова должны быть раздеелны пробелами: ').lower().split()
    list = [input('Введите на что менять, все слова должны быть раздеелны пробелами: ')]
    count = 0
    with open('file.txt', 'r', encoding='utf-8') as data:
        for line in data:
            for i in line.split():
                if i.lower() in str:
                    count += 1
            if count != len(str) and line != '':
                if line != '':
                    list.append(line)
            count = 0
    with open('file.txt', 'w', encoding='utf-8') as data:
        if len(str) != 0:
            for line in list:
                print(line, file=data)