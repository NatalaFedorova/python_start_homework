def x():
    a = int(input("Реальная часть: "))
    b = int(input("Мнимая часть: "))
    firstnum = complex(a, b)
    return firstnum

def y():
    a = int(input("Реальная часть: "))
    b = int(input("Мнимая часть: "))
    secondnum = complex(a, b)
    return secondnum

def selectoperation():
    global operation
    operation = (input(f'Select operation: +, -, *, /: '))
    if operation == '+' or '-' or '/' or '*':
        return operation
    else:
        print('Invalid syntax')

def res(firstnum, secondnum):
    if  operation == '+':
        result = firstnum + secondnum
        return result
    elif operation == '-':
        result = firstnum - secondnum
        return result
    elif operation == '*':
        result = firstnum * secondnum   
        return result
    elif operation == '/':
        result = firstnum / secondnum
        return result
    else:
        print('invalid syntax')

def record(x, y, res):
    with open('results.txt', 'a') as file:
        file.write(f'{x} {operation} {y} = {res}\n')
    print(f' {x} {operation} {y} = {res}\n ')
    file.close()
