# -*- coding: utf-8 -*-
"""
Created on Tue May 19 15:15:55 2020

@author: Samantha
"""
# Loops and functions
spam = 0

if spam < 5:
    print("In if statement", spam)
    spam = spam + 1

while spam < 5:
    print("In while loop", spam)
    spam = spam + 1

x = "anything" # have to initilaze x
while x != "password": 
    print("Enter strong password to end annoying loop")
    x = input()
    
print("You entered the password correct")

while True:
    print("What is 2 + 2")
    answer = int(input())
    if answer == 4:
        break #pulls us out of loop
print("Out of loop")


for i in range(1, 10, 2): # range (start, stop, increment)
    print("Area for some function")
    print(i)

import sys
while True:
    print("What is 2 + 2")
    answer = int(input())
    if answer == 4:
        sys.exit() #compare with break, closes program
print("Out of loop")

def try_example(divideby):
    try:
        return 5 / divideby
    except ZeroDivisionError:
        print("Error: can't divide by 0")

print(try_example(3))
print(try_example(0))
print(try_example(5))