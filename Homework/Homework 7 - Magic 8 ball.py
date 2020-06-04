# -*- coding: utf-8 -*-
"""
# MAGIC 8-BALL HOMEWORK

Created on Thu Jun  4 09:16:37 2020

@author: Samantha
"""

history = ["Your History is:"]

import random 

def eightball(random_number):
    if random_number == 1:
        response = "Yes."
    if random_number == 2:
        response = "No."
    if random_number == 3:
        response = "Maybe."
    if random_number == 4:
        response = "Likely."
    if random_number == 5:
        response = "Unlikely."
    print(response)
    return(response)

# Starting the 8 ball 
print("WELCOME TO MAGIC 8 BALL\n") # \n increases 

while True: # infinite loop
    print("What would you like to know?")
    question = input()
    random_num = random.randint(1, 5)
    prediction = eightball(random_num) # what the 8 ball predicts
    print("PRESS 1 TO EXIT, PRESS 2 TO SEE HISTORY, PRESS ENTER TO ASK ANOTHER QUESTION")
    decision = input()
    if decision == "1":
        break
    if decision == "2":
        history.append(question + " " + prediction)
        print(history)
        input("Press ENTER to Continue") # so I don't see the promt right away
    else:
        input()

