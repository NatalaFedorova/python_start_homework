# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.

week_day = int(input("Введите цифру от 1 до 7: "))
if week_day >= 1 and week_day <= 5:
    print("Сегодня рабочий день (")
elif week_day == 6 or week_day == 7:
    print("Сегодня выходной!")
else:
    print("Пожалуйста, введите цифру от 1 до 7, где \n 1 - понедельник \n 2 - вторник \n 3 - среда \n 4 - четверг \n 5 - пятница \n 6 - суббота \n 7 - вокресенье")
