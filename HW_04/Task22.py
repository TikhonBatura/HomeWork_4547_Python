# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.


from random import randint
from ordered_set import OrderedSet

n = int(input("\nPlease, enter number of elements in First array: "))
m = int(input("Please, enter number of elements in Second array: "))
list1 = []
for el in range(0, n):
    i = randint(0, 99)
    list1.append(i)

list2 = []
for el in range(0, m):
    i = randint(0, 99)
    list2.append(i)
           
print(f"\nFirst array: {list1}")
print(f"Second array: {list2}\n")

list1.extend(list2)
list1.sort()
# print(list1)

result = OrderedSet(list1)

for i in range(len(result)):
    print(result[i], end=" ")
