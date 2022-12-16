''' Задайте список из вещественных чисел. Напишите программу, 
    которая найдёт разницу между максимальным и минимальным значением 
    дробной части элементов.

    *Пример:*

    - [1.1, 1.2, 3.1, 5.1, 10.01] => 0.19 '''

def task_1():
    lst = list(map(float, input("Введите числа через пробел:\n").split()))
    new_lst = [round(i%1,2) for i in lst if i%1 != 0]
    print(max(new_lst) - min(new_lst))

#task_1()

''' Напишите программу, которая будет преобразовывать десятичное число в двоичное.'''

def task_2():
    number = bin(int(input("Введите число: ")))
    print(number)

#task_2()

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
def task_3():
    num_string = str(input("Введите вещественное число: ")).replace(".", "").replace("0", "")
    sum = 0
    for i in range(len(num_string)):
        sum = sum + int(num_string[i])
    print(sum)
#task_3()  

''' Задайте последовательность чисел. Напишите программу,
    которая выведет список неповторяющихся элементов исходной последовательности.'''

def task_4():
    num_list = [randint(0, 10) for i in range(10)]
    print(num_list)
    resalt_list = []
    for i in range(0, len(num_list)):
        if num_list.count(num_list[i]) == 1:
            resalt_list.append(num_list[i])
    print(resalt_list)  

#task_4()          
