# ** Дополнительно **
# 1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где

# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

# Требуется найти N-е число Фибоначчи

def num_fib (n):

    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return num_fib(n-1) + num_fib(n-2)

n = int(input("Please enter number n: "))
print(f"Fibonacy n = {num_fib(n)}")