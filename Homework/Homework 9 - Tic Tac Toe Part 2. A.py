# -*- coding: utf-8 -*-
"""
Updated Tic-Tac-Toe Board
-can check if there is a winner or board is full
@author: Samantha
"""

# Variables and Functions
board = {'1': ' ', '2': ' ', '3': ' ', #this makes the board a dictionary
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' '}

turn = 'X' #used later to initiate start of game 

#board_list_values = list(board.values()) makes the dictionary a list, can evaluate

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

def areSpotsFull(pos, let): #pos is the position on the board
    if pos["1"] and pos["2"] and pos["3"] and pos["4"] and pos["5"] and pos["6"] and pos["7"] and pos["8"] and pos["9"] != " ": 
        print("All spots are full, it is a Cat's Game!")
        return True
      
#Starting the Game

print("Welcome to Tic-Tac-Toe!\n")
input("Press ENTER to begin\n")

while True:
    for i in range(20): #needs for loop, needs to be bigger than 9 in case someone messes up        
        board_coordinates(board)
        print_board(board)
        areSpotsFull(board, turn)
        if areSpotsFull(board, turn) == True:
            break
        print("\nPlayer " + turn + "'s turn. Which position would you like to choose?\nPick a spot 1 - 9.")
        move = input()
        board[move] = turn #this assigns X or O to the position and makes it appear on the screen       
        if turn == "X": #this helps switch the turns between players
           turn = "O"
        else:
            turn = "X"     
    print("Press ENTER to play again OR 1 to EXIT")
    choice = input()
    if choice == "1":
        break
    else: #this code allows me to play again only on
        board = {'1': ' ', '2': ' ', '3': ' ', 
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' '}
        