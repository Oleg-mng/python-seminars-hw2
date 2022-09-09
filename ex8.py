# Задача 8
# Задайте список из k чисел последовательности
#  (1 + 1\k)^k и выведите на экран их сумму.

# k = int(input('Введите число k: '))
# form = 0
# sum_form = 0
# for i in range(1, k+1):
#     form = round((1+1/i)**i, 2)
#     sum_form+=form
#     print(form, end=', ')
# print()
# print('сумма элементов равна: ', sum_form)

k = int(input('Введите число k: '))
list=[]
for i in range (1, k+1):
    list.append(round((1+1/i)**i, 2))
print(list)
print('сумма элементов списка: ', sum(list))