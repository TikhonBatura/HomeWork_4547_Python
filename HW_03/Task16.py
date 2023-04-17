# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 3 2 3 7 5
# Ввод: 3
# -> 2

from random import randint

N = int(input("\nPlease enter number of elements in array: "))
count = 0
list = []
for el in range(0, N):
    i = randint(0, N)
    list.append(i)
           
print(f"\n{list}")

X = int(input("\nPlease enter number which you would like to find: "))

for i in range(0,len(list)):
    if list[i] == X:
        count +=1 

print(f"\nNumber {X} found in list {count} times.\n")


