# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
import c as c
print("Задача 1:")
x = input("X = ")
y = 0
for d in x:
    y += int(d)
print(y)

# Задача 2: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10
print("Задача 2:")
j = int(input('j = '))
print(f'Катя сделала {(j // 3) * 2}')
print(f'Петя и Серёжа, каждый сделал по {j // 6}')

# Задача 3: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no
print("Задача 3:")
tiket = input('tiket = ')
lucky = 0
for i in tiket:
    lucky += int(i)
if lucky % 2 == 0:
    print('lucky')
else:
    print('don\'t lucky')

# Задача 4: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no
print("Задача 4:")
n = int(input('n = '))
m = int(input('m = '))
k = int(input('k = '))
if k % m == 0 and k <= m * n:
    print('yes')
else:
    print('no')