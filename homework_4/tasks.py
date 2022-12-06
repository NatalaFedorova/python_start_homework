import math
import random
from random import randint


'''Вычислить число ПИ c заданной точностью d
- при d = 0.0001, π = 3.1415.    10^-1 ≤ d ≤ 10^-10'''

def task_1():
    number_pi = str(math.pi)
    print(number_pi)
    print(number_pi[:6])

# task_1()


''' Задайте последовательность чисел. Напишите программу,
    которая выведет список неповторяющихся элементов исходной последовательности.'''

def task_3():
    num_list = [randint(0, 10) for i in range(10)]
    print(num_list)
    resalt_list = []
    for i in range(0, len(num_list)):
        if num_list.count(num_list[i]) == 1:
            resalt_list.append(num_list[i])
    print(resalt_list)            



# task_3()


''' Задана натуральная степень k. 
Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
и записать в файл многочлен степени k(до 6 степени).*

 k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0 '''

def task_4():
    k = int(input("Задайте значение k = "))
    ratio_list = [randint(-100, 100) for i in range(k + 1)]
    print(ratio_list)
    
    # формируем конец строки из последнего коэфициента и = 0
    if ratio_list[-1] == 0:
        ratio_list.pop(-1)
        result_str =" = 0"
    else: 
        result_str = " + " + str(ratio_list.pop(-1)) + " = 0"
    
    # Добовляем в список коэфциентов х в нужной степени
    count = 0
    for i in range(1, k + 1):
        if ratio_list[-i] == 0:
            count += 1
        else:   
            if i == 1:
                ratio_list[-i] = str(ratio_list[-i]) + "*x"
            else:
                ratio_list[-i] = str(ratio_list[-i]) + "*x^" + str(i)
    
    # Удаляем из списка коэфициенты, равные нулю
    if count > 0:
        for i in range(count):
            ratio_list.remove(0)
    
    # Собираем все в строку и уаляем лишние символы        
    print(ratio_list)
    result_str = (" + ".join(ratio_list) + result_str).replace("+ -", "-")
    result_str = (result_str.replace("-", "- ")).replace(" 1*", " ")
    
    # Если многочлен начинается с еденицы
    if result_str[0] == "1" and result_str [1] == "*":
        result_str = result_str[2:]
    print(result_str)

    
    # Записываем результат в файл
    file = open("1.txt", "a")
    file.writelines(result_str + "\n")
    file.close()
   

#task_4()


''' Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов.*
Пример:

            - 2*x² + 4*x + 5 = 0 
            - 5*x² + 2*x + 43 = 0
            - Результат: 7*x^2 + 6*x + 48 = 0 '''
def task_5():
    one = open('homework_4/2.txt', "r")
    first = one.readline()[: -4]
    print(first)
    one.close()
 
    two = open("homework_4/3.txt", "r")
    second = two.readline()[: -4]
    print(second)
    two.close()
    
    def find_ratio(first):
        first_list = (first.replace("- ", "-")).split(" ") 
        c = first_list.count("+")
        for i in range(c):
            first_list.remove("+")
    
        for i in range(len(first_list)):
            if first_list[i].find("*") > -1:
                first_list[i] = first_list[i] [: first_list[i].index("*")]
        return first_list
    
    
    first_list = find_ratio(first)
    second_list = find_ratio(second)
    

    result_list = []
    length = abs(len(first_list) - len(second_list))
    if len(first_list) > len(second_list):
        result_list = first_list[0: len(first_list) - length] 
        first_list = first_list[length:] 
    else:
        result_list = second_list[0: len(first_list) - length]
        second_list = second_list [length:]
    for i in range(len(first_list)):
        result_list.append(int(first_list[i]) + int(second_list[i]))
  
    print(result_list)

    def into_polynomial(ratio_list):        
        k = len(ratio_list) - 1
        if ratio_list[-1] == 0:
            ratio_list.pop(-1)
            result_str =" = 0"
        else: 
            result_str = " + " + str(ratio_list.pop(-1)) + " = 0"
    
        count = 0
        for i in range(1, k + 1):
            if ratio_list[-i] == 0:
                count += 1
            else:   
                if i == 1:
                    ratio_list[-i] = str(ratio_list[-i]) + "*x"
                else:
                    ratio_list[-i] = str(ratio_list[-i]) + "*x^" + str(i)
    
        if count > 0:
            for i in range(count):
                ratio_list.remove(0)
         
        print(ratio_list)
        result_str = (" + ".join(ratio_list) + result_str).replace("+ -", "-")
        result_str = (result_str.replace("-", "- ")).replace(" 1*", " ")
    
        if result_str[0] == "1" and result_str [1] == "*":
            result_str = result_str[2:]
        print(result_str)
        return result_str
    res = into_polynomial(result_list)

    file = open("1.txt", "a")
    file.writelines(res + "\n")
    file.close()


task_5()    