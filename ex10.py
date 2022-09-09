# Задача 10
# Реализуйте алгоритм перемешивания списка.

list1 = ['goal', 'match', 'purpose', 'time']
list2 = ['resurce', 'deadline', 'compromise', 'success']
for i in range(3):
    list2.append('good job')
    list1.append('good job')
print(list2)
print(list1)
for c in range(1, 6, 2):
    list1.insert(c, 'fine')
print(list1)
