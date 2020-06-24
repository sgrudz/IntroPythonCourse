# -*- coding: utf-8 -*-
"""
Dictionary Work

@author: Samantha
"""

mouse_time = {'Mouse 1': [5, 2, 5],
              'Mouse 2': [7, 10, 4],
              'Mouse 3': [13, 45, 8]
              } #swirly brackets at bottom

print(mouse_time)
print(mouse_time['Mouse 1']) #prints everything in the key
print(mouse_time['Mouse 2'][0]) #prints whatever index of what list in the key


def print_dict():
    for i in range(len(mouse_time['Mouse 3'])): #len gives the length, need it as a number
        print('Index ' + str(i) + ' is ' + str(mouse_time['Mouse 3'][i]))
        
print_dict()

mouse_stats = {'Mouse 1': {'trait': 'fat', 'color': 'white'},
               'Mouse 2': {'trait': 'smol', 'color': 'blue'}
              }

print(mouse_stats)
print(mouse_stats['Mouse 2']['trait'])

def some_func(local_x):
    local_x += 5
    return local_x

global_x = 0

for i in range(3):
    print("Before function call ", global_x)
    some_func(global_x)
    print("After function call ", global_x)

#the function below is much better, otherwise variable does not update
for i in range(3):
    print("Before function call ", global_x)
    global_x = some_func(global_x)
    print("After function call ", global_x)

# Table 6-1 on page 124

fact = 'Ben is super cool'

print(fact)
print(fact.lower()) # made all lower case
print(fact.upper()) # everything is upper case

fact = fact.lower()

print(fact.islower()) #will evaluate to True if all is lower, also is upper. numbers are always false

# on own, review isalpha(), isalnnum(), isdecimal(), istitle()
# page 129 and 130

fact2 = 'Ben is super strong'
print(fact2.startswith('ben')) #case senstiive, also have endswith as well

bens_stats = ['strong', 'cool', 'funny']
stats = ' '.join(bens_stats)
print(stats)

print('Ben'.rjust(20))
print('Ben'.ljust(20))
print('Ben'.center(20, '*')) #very pretty

# look up strip(), rstrip(), lstrip(): take away white space --> print.strip
# pyperclip allows you to access clipboard (copy/paste)