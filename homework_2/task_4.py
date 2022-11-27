# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import random
from random import randint
n = int(input("Введите число n больше 10: "))
if n <= 10:
    print ("!!! Введите число n больше 10 !!! ")
else:
    new_list = []
    for i in range(n):
        new_list.append(randint(-n, n))
    print (new_list)
    f = open('python_start_homework/homework_2/file.txt', 'r')
    print(new_list[int(f.readline())] * new_list[int(f.readline(2))] * new_list[int(f.readline(3))])
