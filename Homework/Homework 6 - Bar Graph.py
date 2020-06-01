# -*- coding: utf-8 -*-
"""
Bar Graph Homework

Created on Mon Jun  1 10:40:59 2020

@author: Samantha
"""

import matplotlib.pyplot as plt


# data

people = ["Lonzo Ball", "Loren Gray", "Ben Grudzien", "George Lopez"]
coolness = [35, 45, 95, 70]

# formatting
colors =('lavender','pink','plum','lightcoral') # color list found at https://matplotlib.org/3.1.0/gallery/color/named_colors.html
ticks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] # y axis ticks
wid = [0.5, .75, 1, .2] # have numbers less than 1

# plt. functions
plt.bar(people, coolness, width=wid ,align='center', color=colors) # to change color,  use color=()

plt.xticks(people)
plt.xlabel("People")

plt.yticks(ticks)
plt.ylabel("Coolness Level")

plt.title("How cool is Ben? (100 coolness = coolest person ever to live)")


