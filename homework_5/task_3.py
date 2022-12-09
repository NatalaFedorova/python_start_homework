'''Создайте программу для игры в ""Крестики-нолики"".'''
def tic_tac_toe():

    playing_field = ["_", "_", "_"],["_", "_", "_"],["_", "_", "_"]
    players = ["X", "O"]
    counter = 0
    counter_move = 0
    game_over = False

    while game_over == 0:
        
        if counter > 9:
            print("Ничья")
            break
        
        
        for row in playing_field:
            print(" | ".join(map(str, row)))
         
        if counter > 1:
            counter= counter % 2
        
        r, c = [int(i) for i in input(f"Выберете строку и столец для {players[counter]} через пробел: ").split()]
        if r > 0 and c > 0 and r < 4 and c < 4 and playing_field[r - 1][c - 1] == "_":
            playing_field[r - 1] [c - 1] = players[counter]
            counter += 1
            counter_move += 1
        else:
            print("Такой ход сделать нельзя. ")

        for i in range(len(players)):
            for j in range(len(playing_field)):
                if playing_field[j][0] == playing_field[j][1] == playing_field[j][2] == players[i] or playing_field[0][j] == playing_field[1][j] == playing_field[2][j] == players[i]:
                    game_over = 1   
            if playing_field[0][0] == playing_field[1][1] == playing_field[2][2] == players[i] or playing_field[0][2] == playing_field[1][1] == playing_field[2][0] == players[i]:
                game_over = 1
        if counter_move == 9:
            game_over = 2

    
    for row in playing_field:
        print(" | ".join(map(str, row)))
    if game_over == 1:
        counter = (counter + 1) % 2
        print(f"Победили {players[counter]} !")
    else:
        print("Ничья!")  
    

    
tic_tac_toe()