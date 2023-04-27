# Задача 26:  Посчитать факториал (произведение 1 до N) 
# и треугольное число (сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов


def fact (n): # def fact (n) - функция по нахождению факториала для числа n.
    
    if n == 0:
        return 1
    
    return n*fact(n-1)

def trig_num (n): # def trig_num (n) - функция по нахождению треугольного числа для n.
    if n == 1:
        return 1
    
    return n + trig_num (n-1)
    
N = int(input("Please input some number: "))

print(fact(N))
print(trig_num(N))