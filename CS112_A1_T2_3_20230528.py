# File: CS112_A1_T2_3_20230528.py
# Purpose: Task 2 Game 3 
# Author: Shahd Ayman Refaat
# ID: 20230528
# Function to determine valid moves
import random

def valid_moves(coins):
    moves = []
    x = 1
    # Loop to find square numbers less than or equal to the number of coins
    while x * x <= coins:
        moves.append(x * x)
        x += 1
    return moves
# Function for a player to make a move
def player_move(player, coins):
    """ the player has to make a move."""
    print(f"Player {player}, it's your turn.")
    print("Here are the available moves:", valid_moves(coins))
    print("The number of coins is", coins)
    while True:
        try:
            move = int(input("Enter the number of coins you want to take: "))
            if move <= 0:
                print("Please enter a positive integer")
                continue
        except ValueError:
                print("Please enter a valid integer, not a string")
                continue

        #check if the move is valid
        moves = valid_moves(coins)
        if move in moves:
            return move 
        else: 
            print("Invalid move. Please select a valid move") 

def main():
    while True:
        option = input("press A to pick a number or B for random selection: ")
        if option.upper() == "A":
            while True:        
                try:
                    coins = int(input("Enter the number of coins in the pile: "))
                    if coins <= 0:
                        print("Please enter a positive integer")
                        continue
                    elif coins in valid_moves(coins):
                        print("Please enter a number that is not a perfect square")
                        continue
                    break
                except ValueError:
                    print("please enter a valid integer")
            break
        elif option.upper() == "B": 
            coins = random.randint(100,500)
            break
        else: print("please select from A or B")
        
    # Game loop
    while coins > 0:
        # Player 1's move
        move = player_move(1, coins)
        coins -= move
        print(f"Player 1 takes {move} coins. Remaining coins: {coins}")
        if coins <= 0:
            print("Player 1 wins!")
            break

        # Player 2's move
        move = player_move(2, coins)
        coins -= move
        print(f"Player 2 takes {move} coins. Remaining coins: {coins}")
        if coins <= 0:
            print("Player 2 wins!")
main() 
