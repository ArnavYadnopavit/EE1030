import numpy as np
import matplotlib.pyplot as plt

# Load points from the file
points = np.loadtxt('parab.dat', delimiter=',', max_rows=len(list(open("./parab.dat")))-1)

# Extract x and y values
x = points[:, 0]
y = points[:, 1]

# Define points A, B, C, D
x1 = np.array([0, 0])
x2 = np.array([4, 2])

# Plot the parabola
plt.plot(x, y, label='Parabola')
# Plot the specific points
plt.scatter(x1[0], x1[1], color='green', marker='o', label='Point $X_1(0,0)$')
plt.scatter(x2[0], x2[1], color='red', marker='o', label='Point $X_2(4,2)$')

line_y=x * 0.5
plt.plot(x, line_y, color='green', label='Line: x = 2y')
plt.text(x1[0] + 0.2, x1[1] - 0.3, '$X_1(0,0)$', color='green', fontsize=9)
plt.text(x2[0] + 0.2, x2[1] - 0.3, '$X_2(4,2)$', color='red', fontsize=9)
plt.fill_between(x,y,line_y,where=(y >= line_y), color='blue', alpha=0.3, label='Shaded Region')

# Label the axes and add a title
plt.xlabel("x")
plt.ylabel("y")
plt.title("Parabola, Line, and Points $X_1$ & $X_2$")
plt.grid(True)
plt.legend(loc='upper right')
plt.axis('equal')

# Save the plot to a file
plt.savefig('../figs/fig.png')
plt.show()

