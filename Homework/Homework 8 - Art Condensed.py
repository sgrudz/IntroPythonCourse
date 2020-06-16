# -*- coding: utf-8 -*-
"""
Art Homework Clean Version
@author: Samantha
"""

from art import *
import random 

art_list = ["hug me", "fish", "butterfly", "mouse", "monkey", "waves", "cry", "in love"]
def artgenerator(random_number):
    aprint(art_list[random_number - 1])

print("WELCOME TO SAMANTHA'S FUN ART \n") 
input("PRESS ENTER TO SEE FUN ART \n")
previous_num = 101 #cannot be 1 - 8

while True: 
    random_num = random.randint(1, 8)
    x = random_num == previous_num 
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
