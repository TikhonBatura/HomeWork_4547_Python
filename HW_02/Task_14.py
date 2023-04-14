# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input("Please enter number N: "))
result = 0
i = 0
while result < N:
    print(f"2**{i} = {result}")
    result = 2**i
    i+=1
