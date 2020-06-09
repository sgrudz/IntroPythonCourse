# -*- coding: utf-8 -*-
"""
# MAGIC 8-BALL HOMEWORK Fancy.2

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
print("WELCOME TO MAGIC 8 BALL\n") # \n adds a blank line

while True: # infinite loop
    print("What would you like to know?")
    question = input()
    random_num = random.randint(1, 5)
    prediction = eightball(random_num) # what the 8 ball predicts
    print("PRESS 1 TO EXIT, PRESS 2 TO SEE HISTORY, PRESS ENTER TO ASK ANOTHER QUESTION\n")
    history.append(question + " " + prediction) #need to make sure that is outside the if statements
    decision = input() #decision about what participant wants to do
    if decision == "1":
        break
    if decision == "2":
        print(history, "\n")
        print("PRESS ENTER TO ASK ANOTHER QUESTION OR 2 TO EXIT\n") # I like being able to exit after history
        decision2 = input()
        if decision2 == "2":
            break
        


