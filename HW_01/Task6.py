# # # Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# # Вам требуется написать программу, которая проверяет счастливость билета.


n = 6
ticket_number = list(int(num) for num in input("Пожалуйста введите номер билета разделяя числа пробелом: ").strip().split( ))[:n]

print("\n")
print("Номер билета: ", ticket_number)

sum1 = 0
sum2 = 0
for i in range(0, 3):
    sum1 += ticket_number[i]
#     print("sum1 = ", sum1)
for i in range(3, n):
    sum2 += ticket_number[i]
#     print("sum2 = ", sum2)
if sum1 == sum2:
    print("Ура! Вам попался счастливый билет =)")
    print("\n")
else:
    print("Увы, ваш билет обычный, как серый будний день...")
    print("\n")