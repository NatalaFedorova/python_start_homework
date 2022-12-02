import random
import math

''' Напишите программу, которая найдёт произведение пар чисел списка. 
    Парой считаем первый и последний элемент, второй и предпоследний и т.д.

    *Пример:*

    - [2, 3, 4, 5, 6] => [12, 15, 16];
    - [2, 3, 5, 6] => [12, 15] '''

def task_1():
    len_list = random.randint(3, 10)
    example_list = []
    for i in range(len_list):
        example_list.append(random.randint(0, 20))
    print(example_list)

    multy_list = []
    for i in range(math.ceil(len_list / 2)):
        multy_list.append(example_list[i] * example_list[len_list - 1 - i])
    print(multy_list)

# task_1()

''' Задайте список из вещественных чисел. Напишите программу, 
    которая найдёт разницу между максимальным и минимальным значением 
    дробной части элементов.

    *Пример:*

    - [1.1, 1.2, 3.1, 5.1, 10.01] => 0.19 '''

def task_2():
    len_f_list = random.randint(5, 10)
    f_list = []
    for i in range(len_f_list):
        f_list.append(round(random.uniform(-10, 10), 3))
    print(f_list)

    max_i = abs(f_list[0] - int(f_list[0]))
    min_i = max_i
    for i in range(len_f_list):
        f_list[i] = round((abs(f_list[i] - int(f_list[i]))), 3)
        if f_list[i] > max_i:
            max_i = f_list[i]
        if f_list[i] < min_i:
            min_i = f_list[i]
    print(f"Максимальная дробная часть = {max_i} \nМинимальная дробная часть = {min_i} \nРазница равна {round((max_i - min_i), 3)}")

# task_2()

''' Напишите программу, которая будет преобразовывать десятичное число в двоичное.

    *Пример:*

    - 45 -> 101101
    - 3 -> 11
    - 2 -> 10 '''


def task_3():
    number_10 = int(input("Введите число: "))
    number_2_list = []
    if number_10 == 0:
        number_2 = 0
    else:
        while number_10 / 2 > 0:
            number_2_list.insert(0, number_10 - (number_10 // 2) * 2)
            number_10 = number_10 // 2
        number_2 = int(str(number_2_list)[1: -1].replace(", ", ""))
    print(number_2)
    

# task_3()

''' Задайте число. Составьте список чисел Фибоначчи, 
    в том числе для отрицательных индексов.

для k = 8 список будет выглядеть так: 
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] '''

def task_4():
    k = int(input("Введите число: "))
    fib_list = [0, 1]
    for i in range(2, k + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    j = 0
    for i in range(1, k + 1):
        fib_list.insert(0, (-1)**(i + 1) * fib_list[i + j])
        j += 1    
    print(fib_list)

# task_4()

