# Задача 18: Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 1 2 6 4 9
# Ввод: 8
# -> 9

from random import randint

N = int(input("\nPlease enter number of elements in array: "))
X = int(input("\nPlease enter number ""X"": "))
list = []
searchNumMax = 0
searchNumMin = 0
for el in range(0, N):
    i = randint(0, N)
    list.append(i)

for i in range(0,len(list)):
    if list[i] == X+1:
        searchNumMax = list[i]
    elif list[i] == X-1:
        searchNumMin = list[i]

print(f"\n{list}")
if searchNumMax == 0 and searchNumMin == 0:
    print("We didn't found ANY nearest numbers in current lits.")
elif searchNumMin == 0:
    print(f"\nThe nearest to X number in list = {searchNumMax}\n")
elif searchNumMax == 0:
    print(f"\nThe nearest to X number in list = {searchNumMin}\n")
else:
    print(f"\nThe nearest to X\nMIN number = {searchNumMin}\nMAX number = {searchNumMax}")