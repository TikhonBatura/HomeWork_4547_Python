# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

from random import randint

n = int(input("\nPlease, enter number of elements in array: "))
el_min = int(input("Please, enter minimal value: "))
el_max = int(input("Please, enter maximal value: "))

task32_list = []
for el in range(0, n):
    i = randint(-15, 20)
    task32_list.append(i)
count = 0

print(f"\n{task32_list}")
print(f"index from list where {el_min} < value < {el_max}\n")

for i in range(len(task32_list)):
    if el_min <= task32_list[i] <= el_max:
        print(i, end=" ")
