# -*- coding: utf-8 -*-
"""
Voltage Divider Calculator - Basic

Created on Tue May 19 18:51:05 2020

@author: Samantha
"""

input("Enter Vin, R1, and R2 [PRESS ENTER TO BEGIN]")

print("What is input voltage, Vin?")
Vin = int(input())

print("What is R1's value?")
R1 = int(input())

print("What is R2's value?")
R2 = int(input())

def func(): #Ben, I do not know when I put things in these parethesis or not
    Num = Vin*R2
    Dem = R1+R2
    try:
        Vout = Num/Dem
        print("The output voltage =", Vout)
    except ZeroDivisionError:
        print("Error: Can't divide by 0")

output = func()

input("PRESS ENTER TO EXIT")
    