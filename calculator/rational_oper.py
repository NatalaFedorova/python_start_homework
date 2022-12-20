

def x():
    firstnum = float(input('Первое вещественное число: ').replace(',', '.'))
    return firstnum

def y():
    secondnum = float(input('Второе вещественное число: ').replace(',', '.'))
    return secondnum

def selectoperation():
    global operation
    operation = (input(f'Select operation: +, -, *, /: '))
    if operation == '+' or '-' or '/' or '*':
        return operation
    else:
        print('Неверный ввод')

def res(firstnum, secondnum):
    if  operation == '+':
        res = firstnum + secondnum
        result = round(res, 3)
        return result
    elif operation == '-':
        res = firstnum - secondnum
        result = round(res, 3)
        return result
    elif operation == '*':
        res = firstnum * secondnum
        result = round(res, 3)
        return result
    elif operation == '/':
        res = firstnum / secondnum
        result = round(res, 3)
        return result
    else:
        print('invalid syntax')


def record(firstnum, secondnum, result):
    with open('results.txt', 'a') as file:
        file.write(f' {firstnum} {operation} {secondnum} = {result}\n')
    print(f' {firstnum} {operation} {secondnum} = {result}\n ')
    file.close()
    