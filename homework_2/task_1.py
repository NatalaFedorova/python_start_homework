# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = float(input("Введите вещественное число: "))
num_string = str(number).replace(".", "")
print(num_string)
sum = 0
for i in range(len(num_string)):
    sum = sum + int(num_string[i])
print(sum)


