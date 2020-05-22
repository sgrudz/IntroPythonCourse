# -*- coding: utf-8 -*-
"""
Voltage Divider Calculator - Basic

Created on Tue May 19 18:51:05 2020

@author: Samantha
"""
while True:
    input("Enter Vin, R1, and R2 [PRESS ENTER TO BEGIN]")
    
    print("What is input voltage, Vin?")
    Vin = int(input())
    
    print("What is R1's value?")
    R1 = int(input())
    
    print("What is R2's value?")
    R2 = int(input())
    
    def func(): #You put the variables in to pass in the ()
        Num = Vin*R2
        Dem = R1+R2
        try:
            Vout = Num/Dem
            print("The output voltage =", Vout)
        except ZeroDivisionError:
            print("Error: Can't divide by 0")
    
    output = func()
    
    input("PRESS ENTER TO RESTART OR CTRL+C TO EXIT")
    