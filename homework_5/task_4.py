'''Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.'''

def rle_encode(data):
    encoding = '' 
    before_char = '' 
    counter = 1 
    if not data: return '' 

    for char in data:
        if char != before_char:
            if before_char: 
                encoding += str(counter) + before_char
            counter = 1
            before_char = char
        else:
            counter += 1
    else:
        encoding += str(counter) + before_char
        return encoding

f_one = open("python_start_homework/homework_5/1.txt", "r")
data = f_one.read()
f_one.close()
rle_encode(data)
f_two = open("2.txt", "w")
f_two.write(rle_encode(data))
f_two.close()

        
