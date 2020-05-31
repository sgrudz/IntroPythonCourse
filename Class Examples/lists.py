# -*- coding: utf-8 -*-
"""
Created on Sun May 31 19:02:00 2020

@author: Samantha

Harsh Environment: Mouse Drug Experiment
"""

import matplotlib.pyplot as plt

# X axis data
days = [1, 2, 3, 4] # created a list for days

# Y axis data
alive_mice_with_drug = [20, 18, 6, 1]
alive_mice_without_drug = [20, 19, 15, 10]

alive_mice_with_drug_error = [0, 2, 0.5, 1]
alive_mice_without_drug_error = [0, 0, 2, 1]

plt.errorbar(days, alive_mice_with_drug, yerr = alive_mice_with_drug_error, fmt='-x') 
plt.errorbar(days, alive_mice_without_drug, yerr = alive_mice_without_drug_error, fmt='-^') 


"""
plt.plot(days, alive_mice_with_drug, marker = "*")
plt.plot(days, alive_mice_without_drug, marker = "^")
"""

day_labels = ["day 1", "day 2", "day 3", "day 4"]
plt.xticks(days, day_labels)
plt.xlabel("Total Days")
plt.ylabel("Live Mice")
plt.title("Harsh Environment: Mouse Drug Experiment")
plt.legend(["Mice with Drugs", "Mice without Drugs"], loc = "lower left") # need lowercase letters
