# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input("Введите номер четверти: "))
if number == 1:
    print (f"Для всех точек {number} четверти x > 0, y > 0")
elif number == 2:
    print (f"Для всех точек {number} четверти x < 0, y > 0")
elif number == 3:
    print (f"Для всех точек {number} четверти x < 0, y < 0")  
elif number == 4:
    print (f"Для всех точек {number} четверти x > 0, y < 0")
else:
    print ("Введите чисто от 1 до 4")