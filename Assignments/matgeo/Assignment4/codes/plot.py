import numpy as np
import matplotlib.pyplot as plt
import os

points = np.loadtxt("triangle_points.txt", delimiter=',')

x = points[:, 0]
y = points[:, 1]

x_full = np.append(x, [x[0]])
y_full = np.append(y, [y[0]])
ABx=x_full[0:12]
ABy=y_full[0:12]
BCx=x_full[11:24]
BCy=y_full[11:24]
ACx=x_full[22:34]
ACy=y_full[22:34]
# Plot the triangle
plt.figure()
plt.plot(ABx, ABy, label='AB\'')
plt.plot(BCx, BCy, label='BC\'')
plt.plot(ACx, ACy, label='CA\'')

points = np.loadtxt("triangleo_points.txt", delimiter=',')

xo = points[:, 0]
yo = points[:, 1]

xo_full = np.append(xo, [xo[0]])
yo_full = np.append(yo, [yo[0]])
ABxo=xo_full[0:12]
AByo=yo_full[0:12]
BCxo=xo_full[11:24]
BCyo=yo_full[11:24]
ACxo=xo_full[22:34]
ACyo=yo_full[22:34]
# Plot the triangle
plt.plot(ABxo, AByo,linestyle='dotted', label='AB')
plt.plot(BCxo, BCyo,linestyle='dotted', label='BC')
plt.plot(ACxo, ACyo,linestyle='dotted', label='CA')
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()

print(xo_full)
plt.annotate("B", (0,0) ,textcoords="offset points", xytext=(0, 10), ha='center')
plt.annotate("A", (2.500000,4.330127) ,textcoords="offset points", xytext=(0, 10), ha='center')
plt.annotate("C", (6.000000,0.000000),textcoords="offset points", xytext=(0, 10), ha='center')
plt.annotate("A\'", (1.785714,3.092948) ,textcoords="offset points", xytext=(0, 10), ha='center')
plt.annotate("C\'", (4.285714,0.000000) ,textcoords="offset points", xytext=(0, 10), ha='center')

# Save the plot to figs directory
plt.savefig('../figs/fig.png')
plt.show()
