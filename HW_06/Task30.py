# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input("Please, enter 1th element a1: "))
d = int(input("Please, enter measure of step: "))
n = int(input("Please, enter hoq much elements would you like to see: "))
print()
i = 1
arith_prog = []
while i <= n:
    print(f"Element {i} = {a1}")
    arith_prog.append(a1)
    a1 = a1 + d
    i += 1
print(f"\nResult list: {arith_prog}\n")