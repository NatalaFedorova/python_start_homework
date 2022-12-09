import random


'''Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""'''


all_sum = 150
conditions = 50
print(f"На столе {all_sum} конфет(а). Вы можете взять не больше {conditions}")

def for_two_players(all_sum, conditions):
    player_list = ["Ход первого игрока: ", "Ход второго игрока: "]
    counter = random.randint(0,1)
    while all_sum > 0:
        i = counter if counter < 2 else counter % 2
        move = int(input(player_list[i]))
        if move <= 0 or move > conditions or move > all_sum:
            print("Неверный ход. Повторите попытку.")
        else:
            all_sum -= move
            counter += 1
            print(f"Осталось {all_sum} конфет")
    victor_list = ["первый", "второй"]
    print(f"Игра окончена. Победил {victor_list[(counter - 1) % 2]} игрок! Поздравляем!")

#for_two_players(all_sum, conditions)

def for_silly_bot(all_sum, conditions):
    counter = random.randint(0,1)
    while all_sum > 0:
        if counter % 2 == 0: 
            move = int(input("Ваш ход: ")) 
        else: 
            move = random.randint(1, conditions)
            print(f"Ход комтьютера: {move}")
        if move <= 0 or move > conditions or move > all_sum:
            print("Неверный ход. Повторите попытку.")
        else:
            all_sum -= move
            counter += 1
            print(f"Осталось {all_sum} конфет")
    victor_list = ["Вы победили! Поздравляем!", "Победил компьютер!"]
    print(f"Игра окончена. {victor_list[(counter - 1) % 2]}")

#for_silly_bot(all_sum, conditions)       
       
def for_smart_bot(all_sum, conditions):
    counter = random.randint(0,1)
    while all_sum > 0:
        if counter % 2 == 0: 
            move = int(input("Ваш ход: ")) 
        else: 
            move = all_sum % 29 if all_sum % (conditions + 1) > 0 else random.randint(1, conditions)      
            print(f"Ход комтьютера: {move}")
        if move <= 0 or move > conditions or move > all_sum:
            print("Неверный ход. Повторите попытку.")
        else:
            all_sum -= move
            counter += 1
            print(f"Осталось {all_sum} конфет")
    victor_list = ["Вы победили! Поздравляем!", "Победил компьютер!"]
    print(f"Игра окончена. {victor_list[(counter - 1) % 2]}")

#for_smart_bot(all_sum, conditions)     


#for_two_players(all_sum, conditions)
#for_silly_bot(all_sum, conditions)
#for_smart_bot(all_sum, conditions)