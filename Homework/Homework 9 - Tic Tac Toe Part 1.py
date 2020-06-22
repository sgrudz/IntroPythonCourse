# -*- coding: utf-8 -*-
"""
Tic-Tac-Toe Board 1
@author: Samantha
"""

# Variables and Functions
board = {'1': ' ', '2': ' ', '3': ' ', #this makes the board a dictionary
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' '}

turn = 'X' #used later to initiate start of game 

def board_coordinates(board): # designed for easy play
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
input("Press ENTER to begin!\n")

while True:
    for i in range(9): # 9 max moves
        print("\nPlayer " + turn + "'s turn.\n")
        board_coordinates(board)
        print("Which position would you like to choose, Player" + turn +"?\n")
        print_board(board)
        move = input()
        board[move] = turn #list
        if isWinner(board, turn) == True: #here, the board variable outlines a position, and turn is the X or O letter
            print_board(board)
            print("\nPlayer " + turn + " won!\n")
            break
        if turn == "X": #this helps switch the turns between players
            turn = "O"
        else:
            turn = "X"
    input("Thanks for playing! Press ENTER to exit")
    break