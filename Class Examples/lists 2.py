# -*- coding: utf-8 -*-
"""
Created on Sun May 31 19:37:15 2020

@author: Samantha
"""


num_list = [1, 2, 3] # Note 0 index
print(num_list[1]) # this will print the 1 index, the second value

str_list = ["dog", "pizza", "pink"]
print(str_list[0])

double_list = [[1, 2, 3], ["dog", "pizza", "pink"]]
print(double_list[0]) # the whole list becomes index 0
print(double_list[0][1]) # first [] chooses which list, next [] chooses the index

num_list = [4, 5, 6, 7] # reusing the same variable overwrites it
print(num_list[1])
print(num_list[1:]) #includes 1st index and prints everything after
print(num_list[2:]) #prints everything before but does not include it

total_list = num_list + str_list #uses updated list
print(total_list)

total_list[0] = 7 # this says the 0 index is now 7
print(total_list)

del total_list[0] #deletes the 0 index, it is just erased
print(total_list)