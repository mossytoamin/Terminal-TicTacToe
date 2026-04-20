#!/usr/bin/python3
#imports
import time

#Global Variables
global player_win
global round 
global winner
global player_number
global players
global game_board

#Dictionary holding the players associated number and their id
players = {}

#The gameboard
game_board = []

#main() handles game initilzation and flow
def main():
    #Intitilzing Variables
    round = 0
    winner = False

    #Welcome message
    print("\nWelcome to Tic-Tac-Toe by Toamin! The game supports any board-size and number of players!!")
    print("The only requirement is the board-size is never smaller than the number of players! Thank you and have fun :)\n")
    print("p.s. try to break the program.. good luck")
    time.sleep(.5)
    clear()

    #Creating Board
    board_size = int(input("How big do we want the board?"))
    clear()
    create_board(board_size)
    draw_board(game_board)
    
    # we dont check if int
    #Gathering Players
    player_number = int(input("How many players are there?"))
    while player_number > board_size:
        player_number = int(input(f"Board size is {board_size}, there must be {board_size} or less players! Try again:"))
    clear()
    
    #Populating the dictionary with player-names and id
    for i in range(1,player_number+1):
        clear()
        draw_board(game_board)
        player_name = input(f"What is player {i}s name?")
        players[f"{i}"] = player_name
        players[f"{player_name}_id"] = i

    #Main game loop
    while winner == False:
        for i in range(1,player_number+1):
            clear()
            print(f"It is round {round}\n")
        
            move(f"{i}",f"{players[f"{i}"]}_id") #lmfao
            is_win, player_win = win_check(game_board)

            if is_win == True:
                winner = True
                print(f"{players[f"{player_win}"]} won the game!\n Congratulations and thanks for playing :)")
                break
            round += 1
    pass

#move([number-associated-with-player], [id-associated-with-player]) prompts a move and updates the board
def move(player_number, player_id):
    check_valid = False

    while check_valid == False:
        draw_board(game_board)
        move_input= input(f"{players[player_number]} it is your turn! Please enter the x & y coordinates of your move:").split()
        clear()
        check_valid, e_message = valid(game_board, move_input)
        print(f"{players[player_number]}!! {e_message}")

    update_board(move_input, players[player_id])
    draw_board(game_board)


def valid(game_board,move):
    #valid[0] = is integer, valid[1] = is free space
    is_valid = [False,False]
   
    #Checks if there were two inputs
    if len(move) < 2:
        return False, "Invalid Input. Not enough entries.\nPlease enter two integers seperated with a space:\n"

    #Checks if inputs were integers
    #e_message is for debugging.
    is_valid[0], e_message = exception_check(move)

    #If not integers, return False (rest of function will break if continued)
    if is_valid[0] == False:
        return False, "Invalid Input. Entry was a non-integer.\nPlease enter two INTEGERS seperated with a space:\n"
   


    #String variation of y-axis location of move (which list we enter)
    y = int(move[1])
    #String variation of x-axis location of move (which index in the list)
    x = int(move[0])

    #Checks if inputed number is in range of board
    if x > (len(game_board) - 1) or y > (len(game_board) - 1):
        return False, "Invalid Input. Entry was out of the board-range.\nPlease enter two Integers seperated with a space:\n"

    #Checks if number inputed was negative (we could just absolute it)
    if x < 0 or y < 0:
        return False, "Invalid Input. Entry was a negative number.\nPlease enter two POSITIVE INTEGERS seperated with a space:\n"

    #Check if a move already exist on that square
    if game_board[y][x] == 0:
        is_valid[1] = True
    else:
        return False, "Invalid move. Square already taken.\nChoose an empty square please (denoted by a 0):\n"

    #Check if both checks were passed
    if is_valid[0] == True & is_valid[1] == True:
        return True, "No exception found. Valid move."

#Checks for errors on given message and what type of data it expects
def exception_check(message):
    for index in message:
        try:
            int(index)
        except Exception as e:
            return False, e
    return True, "No Exception found. Each value in list is an integer."

#update_board([move][players-associated-number])updates gameboard with the players move
def update_board(move, player):
    game_board[int(move[1])][int(move[0])] = player

#create_board(size) creates a playing board of size x size
def create_board(size):
    for i in range(0,size):
        game_board.append([])
        for j in range(0,size):
            game_board[i].append(0)
    pass

#draw_board(board) draws the inputed board to the console with numbered axes
def draw_board(board):
    for i in range(0,len(board)):
        print(f"{board[i]} {i}")
    
    bot_numbers = ""
    for n in range(0,len(board)):
        bot_numbers = f"{bot_numbers} {n} "
    print(bot_numbers)
    print("\n")
    pass
     
#win_check(board) checks if the inputed board has a win by any player
def win_check(board):
    #Horizontal win-check
    for n in board:
        check = []
        for h in range(0,len(board)):
            check.append(n[h])
        if check_list_win(check) == True:
            return True, check[0]
        
    #Verticle win-check
    for j in range(0,len(board)):
        check = []
        for v in board:
            check.append(v[j])
        if check_list_win(check) == True:
            return True, check[0]
        
    #Diagonal Wins
    tl_diagonal = []
    for c in range(0,len(board)):
        tl_diagonal.append(board[c][c])

    bl_diagonal = []
    length = len(board) - 1
    for x in range(length,-1,-1):
        bl_diagonal.append(board[x][abs(length-x)])

    if check_list_win(bl_diagonal) == True:
        print(bl_diagonal)
        return True, bl_diagonal[0]
    
    if check_list_win(tl_diagonal) == True:
        print(tl_diagonal)
        return True, tl_diagonal[0]

    return False, "no winner"

#check_list_win(move_list) used by win_check() to check if an extracted list is a win or not
def check_list_win(move_list):
    #if a 0 no win.
    for d in move_list:
        if d == 0:
            return False
    
    #checking if more than one number in list
    for k in range(1,len(move_list)):
        if move_list[k] != move_list[k-1]:
            return False
        
    return True
        
#clear() adds a bunch of new lines to do a pseudo console clear
def clear():
    for i in range(0,10):
        print("\n")
    
main()
