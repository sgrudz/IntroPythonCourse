# -*- coding: utf-8 -*-
"""
Dictionary Example

@author: Samantha
"""
'''
myCat = {"size": "fat", "color": "grey", "trait": "loud"}
print(myCat["size"])

myDog = {"color": "grey","size": "fat",  "trait": "loud"}
print(myCat == myDog) # order does not matter for dictionaries
'''
# refer to dictionaries based on their keys. no indexing. need to refer to key or value

social_media_account = {"kylie": "insta", "tyga": "twitter", "j cole": "insta"}

while 1: # True = 1. At the end of the day 1s and 0s bumping around
    print("\nEnter a name: (press enter to exit)")
    name = input()
    if name == "":
        break
    if name in social_media_account: # if name in key
        print("\n" + name + " has a " + social_media_account[name] + " page")
    else:
        print("\nWhat is their social media page?")
        social_media = input()
        social_media_account[name] = social_media # value for the key
        print("\ndatabase updated")
    
    # print(social_media_account) # can show updated list in real time