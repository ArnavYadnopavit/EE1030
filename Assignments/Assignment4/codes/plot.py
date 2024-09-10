import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
with open("data.txt", 'r') as f:
    L = f.readlines()
a = []
for line in L:
    row = line.strip().split()
    row = [int(x) for x in row]
    a.append(row)
A=a[0]
B=a[1]
fig, ax = plt.subplots()
ax.plot([A[0], B[0]], [A[1], B[1]], marker='o', linestyle='-', color='blue', label='Line AB')
ax.text(*A, f'A({A[0]}, {A[1]})')
ax.text(*B, f'B({B[0]}, {B[1]})')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()
plt.show()

