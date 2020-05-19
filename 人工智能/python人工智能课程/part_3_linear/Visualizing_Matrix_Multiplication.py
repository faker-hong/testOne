import numpy as np
import matplotlib.pyplot as plt


v = np.array([-1, 2])
i = np.array([1, 0])
j = np.array([0, 1])

# Define v_ihat - as v[0](x) multiplied by basis vector ihat
v_ihat = v[0] * i

# Define v_jhat_t - as v[1](y) multiplied by basis vector jhat
v_jhat = v[1] * j

# vector v_ihat_t added to vector v_jhat_t
v_t = v_ihat + v_jhat

# Define 2x2 matrix ij
ij = np.array([[3, 1],[1, 2]])

# TODO 1.: Demonstrate getting v_trfm by matrix multiplication
# by using matmul function to multiply 2x2 matrix ij by vector v
# to compute the transformed vector v (v_t)
v_t = np.matmul(v, ij)

# Prints vectors v, ij, and v_t
print("\nMatrix ij:", ij, "\nVector v:", v, "\nTransformed Vector v_t:", v_t, sep="\n")

# Plot that graphically shows vector v (color='b') - whose position can be
# decomposed into v_ihat and v_jhat

# Creates axes of plot referenced 'ax'
ax = plt.axes()

# Plots red dot at origin (0,0)
ax.plot(0, 0, 'or')

# TODO 4.: Plot transformed vector v (v_t) a blue colored vector(color='b') using
# vector v's ax.arrow() statement above as template for the plot
ax.arrow(0, 0, *v_t, color='r', linewidth=2.5, head_width=0.30,
         head_length=0.35)

# Plots vector v_ihat as dotted green arrow starting at origin 0,0
ax.arrow(0, 0, *v_ihat, color='g', linestyle='dotted', linewidth=2.5, head_width=0.30,
         head_length=0.35)

# Plots vector v_jhat as dotted red arrow starting at origin defined by v_ihat
ax.arrow(v_ihat[0], v_ihat[1], *v_jhat, color='r', linestyle='dotted', linewidth=2.5,
         head_width=0.30, head_length=0.35)

# Plots vector v as blue arrow starting at origin 0,0
ax.arrow(0, 0, *v, color='b', linewidth=2.5, head_width=0.30, head_length=0.35)


# Sets limit for plot for x-axis
plt.xlim(-4, 2)

# Set major ticks for x-axis
major_xticks = np.arange(-4, 2)
ax.set_xticks(major_xticks)


# Sets limit for plot for y-axis
plt.ylim(-2, 4)

# Set major ticks for y-axis
major_yticks = np.arange(-2, 4)
ax.set_yticks(major_yticks)

# Creates gridlines for only major tick marks
plt.grid(b=True, which='major')

# Displays final plot
plt.show()