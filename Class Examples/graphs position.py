import matplotlib.pyplot as plt
import numpy as np

# X axis data
time = np.arange(-3,14,0.01) # (start, stop, step)

# Y axis data
position = -time**2 + 10*time + 21
velocity = -2*time + 10

# Organize data and initilize the graph
fig, ax1 = plt.subplots()
ax1.plot(time, position, label = "Position")
ax1.plot(time, velocity, label = "Velocity")
ax1.legend()

# Graph labels and design
ax1.grid()
ax1.set(xlabel = "Time (s)", ylabel = "Meters (m)", title = "Position versus Time")
plt.xlim(-2.5,14)
plt.ylim(-17,50)

plt.show()