import numpy as np
import matplotlib.pyplot as plt


# Define vector v
v = np.array([1, 1])
a = 3
w = np.array([-2, 2])
av = a*v
# vectors addition
vw = v+w

# Plots vector v as blue arrow with red dot at origin (0,0) using Matplotlib

# Creates axes of plot referenced 'ax'
ax = plt.axes()

# Plots red dot at origin (0,0)
ax.plot(0, 0, 'or')

# Plots vector v as blue arrow starting at origin 0,0
plt.arrow(0, 0, *v, color='b', linewidth=2.0, head_width=0.2, head_length=0.2)
plt.arrow(0, 0, *av, color='y', linewidth=2.0, head_width=0.2, head_length=0.2)
plt.arrow(0, 0, *vw, color='c', linewidth=2.0, head_width=0.2, head_length=0.2)

# Sets limit for plot for x-axis
plt.xlim(-3, 5)

# Set major ticks for x-axis
major_xticks = np.arange(-3, 6)
ax.set_xticks = major_xticks


# Sets limit for plot for y-axis
plt.ylim(-1, 5)

# Set major ticks for y-axis
majot_yticks = np.arange(-1, 6)
ax.set_yticks = majot_yticks

# Creates gridlines for only major tick marks
plt.grid(which='major', b=True)

# Displays final plot
plt.show()
