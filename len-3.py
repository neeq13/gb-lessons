import random
# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел A i
# . Последняя строка содержит число X

print('Задача 1:')
x = int(input('Длинна массива = '))
a = []
count = 0
for i in range(x):
    a.append(random.randint(0, 10))

temp = int(input('Введите число от 0 до 10 = '))
for i in a:
    if temp == i:
        count += 1
print(count)

# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел A i
# . Последняя строка содержит число X

print('Задача 2:')
x = int(input('Длинна массива = '))
a = []
char = int(input('Заданное число = '))
temp_1 = 0
temp_2 = 0
for i in range(x):
    a.append(random.randint(0, 30))

for i in a:
    if char <= 0:
        print(0)
        exit()
    elif i == char:
        print(i)
        exit()
    elif char > i:
        if temp_1 == 0:
            temp_1 = i
        if temp_1 < i:
            temp_1 = i
    else:
        if temp_2 == 0:
            temp_2 = i
        if temp_2 < i:
            temp_2 = i
if char - temp_1 < temp_2 - char:
    print(temp_1)
elif char - temp_1 == temp_2 - char:
    print(temp_1, temp_2)
else:
    print(temp_2)

# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

print('Задача 3:')
word = input('Введите слова: ')
price = 0
dic_eng = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
dic_rus = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}

for char in word:
    for (key, value) in dic_eng.items():
        for char_value in value:
            if char.upper() == char_value:
                price += key
    for (key, value) in dic_rus.items():
        for char_value in value:
            if char.upper().__eq__(char_value):
                price += key
print(price)