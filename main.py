# My second Python Project (2026-3-11 / Wed):

#import random and sys  
import random
import sys
from guessing_game import name_validation, string_validation, again_validation

def player_validation(first, x_player, o_player):
    while True:
        if first in (x_player, o_player):
            return first

        else:
            print(f"you must type {x_player} or {o_player}")

        first = input(f"Who want to start first ({x_player} or {o_player})? ")

#print the board:
def board_printer(b):
    print(f"+-------+-------+-------+")
    print(f"|       |       |       |")
    print(f"|   {b[0]}   |   {b[1]}   |   {b[2]}   |")
    print(f"|       |       |       |")
    print(f"+-------+-------+-------+")
    print(f"|       |       |       |")
    print(f"|   {b[3]}   |   {b[4]}   |   {b[5]}   |")
    print(f"|       |       |       |")
    print(f"+-------+-------+-------+")
    print(f"|       |       |       |")
    print(f"|   {b[6]}   |   {b[7]}   |   {b[8]}   |")
    print(f"|       |       |       |")
    print(f"+-------+-------+-------+")

#taking the input from the player:
def player_move(b, available, player_type):
    player = input("What's your move? (1-9): ")
    player = validation(b, player)

    b[player] = player_type

    available.remove(player+1)

    result = winner(b, player_type)
    return result

#check if the input is valid:
def validation(b, player):
    while True:
        try:
            player_int = int(player)

            if 1 <= player_int <= 9:
                if b[player_int-1] not in ('X','O'):
                    return player_int -1
                
                else:
                    print("Oops, this spot is already taken")

            else :
                print("Your move must be a number from 1 to 9")
        
        except ValueError:
            print("Your move must be a number from 1 to 9")

        player = input("What's your move? (1-9): ")

#checking if their winner:
def winner(b, play_type):
    win = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
           ]
    
    for x,y,z in win:
        if play_type == b[x] == b[y] == b[z]:
            return True
        
    return False

def type_validation(player_type, t=0):
    while True:
        player_type = player_type.upper()

        if player_type in ('O', 'X'):
            return player_type
        
        else:
            print("You must choose 'X' or 'O'")

        player_type = input("Choose 'X' or 'O': ")
        
#computer turn:
def computer(available):
    return random.choice(available) 

def computer_turn(b, available, computer_move, computer_type):
    b[computer_move-1] = computer_type

    available.remove(computer_move)

    result = winner(b, computer_type)
    return result

#Main:
def main():
    b = [
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9"
         ]
    
    available = [1,2,3,4,5,6,7,8,9]
    
    print("Welcome to the Tic-Tac-Toe game!")

    print("Do you want to play with me or with your friend?")

    playing_type = string_validation(input("For playing with me enter ('Yes'), for playing with friend enter('No'): "))

    if playing_type == 'no':
        print("The person who will choose 'X': ")
        x_player = name_validation(input("Please enter your name: "))

        print("The person who will choose 'O': ")
        o_player = name_validation(input("Please enter your name: "))

        print(f"Ok, now {x_player} will play with 'X', and {o_player} will play with 'O'")
        print("Good luck!")

        player_1 = player_validation(input(f"Who wants to start first ({x_player} or {o_player})? "), x_player, o_player)

        if player_1 == x_player:
            sign_1 = 'X'
            player_2 = o_player
            sign_2 = 'O'

        else :
            player_2 = x_player
            sign_1 = 'O'
            sign_2 = 'X'

        board_printer(b)

        result = False
        while not result and available:
            print(f"Ok {player_1}, your turn now!")

            result = player_move(b, available, sign_1)
            board_printer(b)

            if not result and available:
                print(f"Ok, now {player_2}'s turn!")

                result = player_move(b, available, sign_2)
                board_printer(b)

            elif result:
                print("Winner!")
                print(f"'{player_1}' won!")

                again_validation()

            else :
                print("Tie")

                again_validation()

        if result:
            print("Winner")
            print(f"'{player_2}' won!")

            again_validation()

        else :
            print("Tie")

            again_validation()

    else:
        player_type = type_validation(input("Choose 'X' or 'O': "))

        if player_type == 'O':
            computer_type = "X"
        else :
            computer_type = "O"

        board_printer(b)

        result = False
        while not result and available:
            result = player_move(b, available, player_type)
            board_printer(b)

            if not result and available:
                print("My turn now...")
                computer_move = computer(available)

                print(f"Hmm... I will choose {computer_move}")
                result = computer_turn(b, available, computer_move, computer_type)
                board_printer(b)

            elif result:
                print("Winner!")
                print(f"'{player_type}' won!")
                
                again_validation()
            
            else :
                print("Tie")

                again_validation()

        if result:
            print("Game Over!")
            print(f"'{computer_type}' won!")

            again_validation()

        else :
            print("Tie")

            again_validation()

if __name__ == "__main__" :
    main()