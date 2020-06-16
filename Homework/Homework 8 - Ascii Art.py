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
input("PRESS ENTER TO SEE FUN ART \n") # move outside of while loop so it is not repetitive for choice function
previous_num = 100

while True: # infinite loop
    random_num = random.randint(1, 8)
    x = random_num == previous_num #this will evaluate to True or False
    if x == False:
        artgenerator(random_num)
        #print("previous number did not equal current number")
    else:
        #print("previous number equalled current number")
        if (random_num < 8):
            random_num = previous_num + 1
            #print("<8")
        else:
            random_num = previous_num - 1
            #print("8")
        artgenerator(random_num)
    previous_num = random_num
    print("PRESS ENTER TO SEE MORE FUN ART OR 1 TO EXIT")#allows users to stop seeing fun art
    choice = input()
    if choice == "1":
        break
  
