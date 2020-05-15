# -*- coding: utf-8 -*-
"""
Created on Fri May 15 15:02:29 2020

@author: Samantha
"""


print("What is your name?")
name = input()

def name_func(name):
    if name == "Alice": #needed quotations
        print("Hi, Alice.")
    else:
        print("Hi, ",name,"!")

name_func(name)