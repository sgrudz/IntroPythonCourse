# -*- coding: utf-8 -*-
"""
Tic-Tac-Toe Board
Updated Tic-Tac-Toe Board
    checks if is winner
    can tell if it is a cat game ONLY IF all moves are allowed.
@author: Samantha
"""

# Variables and Functions
board = {'1': ' ', '2': ' ', '3': ' ', #this makes the board a dictionary
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' '}

turn = 'X' #used later to initiate start of game 

def board_coordinates(board):
    print("Position Coordinates of the Board:\n")
    print(" 1" + ' | ' + "2" + ' | ' + "3")
    print('-----------')
    print(" 4" + ' | ' + "5" + ' | ' + "6")
    print('-----------')
    print(" 7" + ' | ' + "8" + ' | ' + "9\n")

def print_board(board):
    print(' ' + board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('-----------')
    print(' ' + board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('-----------')
    print(' ' + board['7'] + ' | ' + board['8'] + ' | ' + board['9'])


def isWinner(pos, let): #pos is the position on the board, let is letter (X or O)
    return((pos["1"] == let and pos["2"] == let and pos["3"] == let) or
           (pos["4"] == let and pos["5"] == let and pos["6"] == let) or
           (pos["7"] == let and pos["8"] == let and pos["9"] == let) or
           (pos["1"] == let and pos["4"] == let and pos["7"] == let) or
           (pos["2"] == let and pos["5"] == let and pos["8"] == let) or
           (pos["3"] == let and pos["6"] == let and pos["9"] == let) or
           (pos["1"] == let and pos["5"] == let and pos["9"] == let) or
           (pos["7"] == let and pos["5"] == let and pos["3"] == let))

#Starting the Game

print("Welcome to Tic-Tac-Toe!\n")
input("Press ENTER to begin\n")

while True:
    for i in range(9): # 9 max moves
        board_coordinates(board)
        print_board(board)
        print("\nPlayer " + turn + "'s turn. Which position would you like to choose?")
        move = input()
        board[move] = turn #this assigns X or O to the position and makes it appear on the screen
        if isWinner(board, turn) == True: #here, the board variable outlines a position, and turn is the X or O letter
            print_board(board)
            print("\nPlayer " + turn + " won!\n")
        if turn == "X": #this helps switch the turns between players
           turn = "O"
        else:
            turn = "X"            
    for i in range(9,10): # what happens when you are outside of 9 moves
        print_board(board) # can see the cat's game board
        print("No more moves left, it is a tie game!\n")
    print("Press ENTER to play again OR 1 to EXIT")
    choice = input()
    if choice == "1":
        break
    else: #this code allows me to play again only on
        board = {'1': ' ', '2': ' ', '3': ' ', 
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' '}
