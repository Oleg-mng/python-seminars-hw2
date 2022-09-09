# Задача 9
# Задайте список из N элементов, заполненных числами из
# промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем
# через пробел позициях.

from random import randint, random

n = int(input('Введите число N: '))
print('вами задан промежуток: ', -n, 'до', +n)
list1 = []
print('заполняем данный список рандомными числами')
for i in range(-n, n+1):
    list1.append(randint(3, 15))
print(list1)
twonumbers = input('Введите позиции чисел, разделенные пробелом: ').split()
num = list(map(int, twonumbers))
print(num)
comp=1
q=0
while q < len(num):
    p=num[q]
    # print(p)
    comp *= list1[p]
    q += 1
print('произведение элементов на указанных позициях: ', comp)
