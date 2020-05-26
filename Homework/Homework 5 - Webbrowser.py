# -*- coding: utf-8 -*-
"""
Created on Fri May 22 16:06:40 2020

@author: Samantha
"""

print("Welcome to your costumized webpage organizer! Below are the listed selctions.")
print("Selection 1: Academic")
print("Selection 2: Work")
print("Selection 3: Social")

import webbrowser

print("Which selection do you wish to open?")
user_input = int(input()) #needed to define the variables outside the function

def launch_website(user_input):
    if user_input == 1:
        webbrowser.open("https://ctools.umich.edu/")
        webbrowser.open("https://wolverineaccess.umich.edu/f/u24l1s13/normal/render.uP")
    if user_input == 2:
        webbrowser.open("https://sites.lsa.umich.edu/samkwon-lab/")
        webbrowser.open("https://myaccount.google.com/")
    if user_input == 3:
        webbrowser.open("https://www.facebook.com/?ref=tn_tnmn")
        webbrowser.open("https://twitter.com/explore")

launch_website(user_input)

input("PRESS ENTER TO CLOSE")