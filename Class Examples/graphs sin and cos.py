# -*- coding: utf-8 -*-
"""
Created on Wed May 27 19:39:34 2020

@author: Samantha
"""
#import a massive block a code with a lot of functions in it
import matplotlib.pyplot as plt
import numpy as np

# X axis data
time = np.arange(0,14,0.01) #arange creates a vector

# Y axis data
cos_function = np.cos(time) # pass time through cosine
sin_function = np.sin(time)

fig, ax = plt.subplots(2) # 2 plots on this one figure. ax is a vector ax[0]
ax[0].plot(time, cos_function, label = "Voltage")
ax[0].legend

ax[1].plot(time, sin_function, label = "Voltage")
ax[1].legend

plt.show