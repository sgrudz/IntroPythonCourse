# -*- coding: utf-8 -*-
"""
Lists 3

Created on Wed Jun  3 19:00:24 2020

@author: Samantha
"""
food = ["hotdog", "milk", "fries"]
print(len(food)) #length of your string

food[1] = food[2] # the first index milk is redefined as the second index, fries 
print(food)

del food[1]
print(food)

for i in range(4): #i will go through four times, start at 0
    print(i)
    
for i in [0,1,2,3]: #same as the prior code
    print(i)

fake_sports = ["soccer", "croquet", "footsie"]

for i in range(len(fake_sports)): #this will cycle through the list and let us know how many indexes
    print("Index " + str(i) + " in fake_sports is " + fake_sports[i]) #need to put str(i)

if "milk" in food:
    print("True")
else:
    print("False")

toolstuff = ["hammer", "wrench", "saw", "nails"]
print(toolstuff.index("wrench")) #this tells you which index it is

toolstuff.append("wood pencil") #adds to end of the list
print(toolstuff)

toolstuff.sort() # alphabetically sorted, not passing anything through since all info is there
print(toolstuff)

num = [3, 50, 1, 90]
num.sort() # need the parenthesis
print(num)

rows = 5
for i in range(0, rows):
    for j in range(0, rows - i - 1):
        print(end = " ")
    for j in range(0, i + 1):
        print("*", end = " ")
    print() #prints a new line
    