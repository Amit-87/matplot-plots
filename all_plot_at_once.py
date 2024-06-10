import matplotlib.pyplot as plt
import random
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Generate random data
np.random.seed(0)  # For reproducibility
x = np.random.randint(20, 90, 20)
y = np.random.randint(20, 90, 20)
u = np.random.randint(-10, 10, 20)
v = np.random.randint(-10, 10, 20)

fig = plt.figure(figsize=(15, 15))

fig.suptitle("MATPLOTLIB PLOTS\n\n",fontsize=26)

# Line Plot
plt.subplot(4, 4, 1)
plt.plot(x, y, color='blue', linestyle='-', marker='o')
plt.title('Line Plot')

# Bar Plot
plt.subplot(4, 4, 2)
xb = ['A','B','C','D','E']
yb = [23,25,34,40,29]
plt.bar(xb, yb, color='pink',edgecolor='black')
plt.title('Bar Plot')

# Histogram
plt.subplot(4, 4, 3)
l = [23,45,34,25,45,29,45,64,69,40,56,12,83,56,78,46,34,90]
plt.hist(l, bins=10, color='cyan', alpha=0.7,edgecolor='purple')
plt.title('Histogram')

# Scatter Plot
plt.subplot(4, 4, 4)
xsc = np.random.randint(20,90,75)
ysc = np.random.randint(20,90,75)
color = np.random.randint(20,90,75)
plt.scatter(xsc, ysc, c = color, cmap='hot')
plt.colorbar()
plt.title('Scatter Plot')

# Pie Chart
plt.subplot(4, 4, 5)
plt.pie(y[:5], labels=x[:5], colors=plt.cm.Paired.colors)
plt.title('Pie Chart')

# Box Plot
plt.subplot(4, 4, 6)
plt.boxplot([x, y], patch_artist=True,
            boxprops=dict(facecolor='red'))
plt.title('Box Plot')

# Violin Plot
plt.subplot(4, 4, 7)
plt.violinplot(y, showmeans=True)
plt.title('Violin Plot')

# Stem Plot
plt.subplot(4, 4, 8)
l = [23,45,34,45,29,45,69,56,12,56,78,46,34,90]
plt.stem(l,linefmt="purple",markerfmt='D',bottom=40)
# plt.stem(y, linefmt='orange', markerfmt='o', basefmt=' ')
plt.title('Stem Plot')

# Step Plot
plt.subplot(4, 4, 9)
xst = ['day1','day2','day3','day4','day5']
yst = np.random.randint(20,30,5)
plt.step(xst, yst, color='brown', where='mid',marker='D')
plt.title('Step Plot')

# Stack Plot
plt.subplot(4, 4, 10)
plt.stackplot(range(len(x)), x, y, colors=['magenta', 'turquoise'])
plt.title('Stack Plot')

# Line and Stem Plot
plt.subplot(4, 4, 11)
xls = [1,2,3,4,5,6,7,8,9]
yls = [34,56,23,67,45,20,38,55,34]
plt.stem(xls, yls, linefmt='hotpink', markerfmt='D', basefmt=' ',bottom=10)
plt.plot(xls, yls, color='purple')
plt.title('Line and Stem Plot')

# Polar Plot
ax_polar = plt.subplot(4, 4, 12, projection='polar')
angles = np.linspace(0, 2 * np.pi, 20)
radii = np.random.randint(20, 90, 20)
ax_polar.plot(angles, radii, color='magenta')
ax_polar.set_title('Polar Plot')

# Hexbin Plot
plt.subplot(4, 4, 13)
plt.hexbin(x, y, gridsize=10, cmap='viridis')
plt.colorbar()
plt.title('Hexbin Plot')

# Quiver Plot
plt.subplot(4, 4, 14)
plt.quiver(x, y, u, v, color='teal')
plt.title('Quiver Plot')

# Contour Plot
plt.subplot(4, 4, 15)
X, Y = np.meshgrid(np.linspace(20, 90, 20), np.linspace(20, 90, 20))
Z = np.sin(X/10) * np.cos(Y/10)
plt.contour(X, Y, Z, colors='black')
plt.contourf(X, Y, Z, cmap='coolwarm', alpha=0.7)
plt.colorbar()
plt.title('Contour Plot')

# 3D Plot
ax_3d = fig.add_subplot(4, 4, 16, projection='3d')
z = np.random.randint(20, 90, 20)
ax_3d.scatter(x, y, z, color='maroon')
ax_3d.set_title('3D Plot')

plt.tight_layout()
plt.show()
