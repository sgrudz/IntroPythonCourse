# -*- coding: utf-8 -*-
"""
Application of Dictionaries
@author: Samantha
"""

# Dungeon Game Inventory Loot System

def add_to_inventory(inventory, added_items): # players dict, dragons list
    for loot in added_items: # loot so we can iterate through added items. represents an integer for each item in the list
        inventory.setdefault(loot, 0) # embedded into python. if item is in list add value to key, else add key and intialize with value 0
        inventory[loot] += 1 #inventory[loot] = inventory[loot] + 1
    return inventory #need to retun or will get none

def display_inventory(inventory): #the two inventories do not relate to each other
    print("\nPretty Inventory")
    item_total = 0 
    for k, v in inventory.items(): #cycle through both 
        print(k + " " + str(v))
        item_total += v #item total = item toltal + v
    print("Total Items: " + str(item_total))

player_inventory = {"gold coin": 7, "sword": 1} # use {} for dictionary. {key: value}
dragon_loot = ["gold coin", "sword", "gold coin", "gold coin"]

print("\nPlayer Inventory")
print(player_inventory)

print("\nDragon Loot")
print(dragon_loot)

player_inventory = add_to_inventory(player_inventory, dragon_loot)
print("\n Updated Player Inventory")
print(player_inventory)

display_inventory(player_inventory)