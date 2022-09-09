# Задача 6
# Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
c = float(input('введите вещественное число: '))
b = int(c)
d = c - b
d = round(d*10, 1)
os = int(d % 10)
sum = 0
while os != 0:
        #print(d, os, sum)
        sum += os
        d = round(d*10, 1)
        os = int(d % 10)
print('сумма чисел после запятой равна = ', sum)
os1 = int(c % 10)
c = round(c/10, 1)
sum1 = 0
while os1 != 0:
    #print(c, os1, sum1)
    sum1 += os1
    os1 = int(c % 10)
    c = round(c/10, 1)
print('сумма чисел до запятой равна = ', round(sum1, 3))
print('Общая сумма его чисел равна = ', round(sum1+sum, 3))
# if d != 0:
#     sum = 0
#     c = round(c*10, 1)
#     os = int(c % 10)
#     while os != 0:
#         print(c, os, sum)
#         sum += os
#         c = round(c*10, 1)
#         os = int(c % 10)
#     print('сумма его чисел равна = ', sum)
# else:
#     os = int(c % 10)
#     c = round(c/10, 1)
#     sum1 = 0
#     while os != 0:
#         print(c, os, sum1)
#         sum1 += os
#         os = int(c % 10)
#         c = round(c/10, 1)
#     print('сумма его чисел равна = ', round(sum1, 3))

