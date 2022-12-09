''' Напишите программу, удаляющую из текста все слова, содержащие ""абв"". '''

test_text = "Функционабвльное программирование предстабвляет собой методику набвписания програбвммного обеспечения, в центре внимабвния которой находятся функции."
test_symbols = "абв"
#text = input("Ваш текст для проверки: ")
#symbols = input("Слова с какими символами удалить? ")
def deltte_words_with_symbols(text = test_text, symbols = test_symbols):
    text_list = text.split()
    result_list = []
    for i in range(len(text_list)):
        if text_list[i].find(symbols) == -1:      
            result_list.append(text_list[i])
    print("Результат: " + " ".join(result_list))

deltte_words_with_symbols()


