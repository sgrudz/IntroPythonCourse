# -*- coding: utf-8 -*-
"""
Art Homework #2

Created on Thu Jun 11 19:47:16 2020

@author: Samantha
"""

from art import *
import random 

def artgenerator(random_number):
    if random_number == 1:
        aprint("hug me")
    if random_number == 2:
        aprint("fish")       
    if random_number == 3:
        aprint("butterfly")
    if random_number == 4:
        aprint("mouse")
    if random_number == 5:
        aprint("monkey")
    if random_number == 6:
        aprint("waves")
    if random_number == 7:
        aprint("cry")
    if random_number == 8:
        aprint("in love")

# Starting the fun art
print("WELCOME TO SAMANTHA'S FUN ART \n") # \n adds a blank line
input("PRESS ENTER TO SEE FUN ART \n")
previous_num = 101 #cannot be 1 - 8

while True: # infinite loop
    random_num = random.randint(1, 8)
    x = random_num == previous_num #this will evaluate to True or False
    if x == True:
         for i in range(1,100): # I do not know how big to make this loop
            random_num = random.randint(1, 8)
            if random_num != previous_num:
                break
    artgenerator(random_num)
    previous_num = random_num
    print("PRESS ENTER TO SEE MORE FUN ART OR 1 TO EXIT")#allows users to stop seeing fun art
    
    choice = input()
    if choice == 1:
        break
