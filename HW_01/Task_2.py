# Задача 2: Найдите сумму цифр трехзначного числа. 

n = int(input(("Please enter 3-digital number: ")))

if n < 1000 and n > 99:
    n1 = int(n % 10)
    n2 = int(n / 10 % 10)
    n3 = int(n / 100 % 10)
    
    print(f"Sum of didgitals in number: {n1 + n2 + n3}")
else:
    print("Input incorrect number")