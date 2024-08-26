import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
with open("data.txt", 'r') as f:
    L = f.readlines()
a = []
for line in L:
    row = line.strip().split()  # Remove leading/trailing whitespace and split by spaces
    row = [int(x) for x in row]  # Convert elements to integers
    a.append(row)

P=a[0]
Q=a[1]
R=a[2]
S=a[3]
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter([P[0], Q[0], R[0]], [P[1], Q[1], R[1]], [P[2], Q[2], R[2]], label=['P', 'Q', 'R','S'])
ax.plot([P[0], S[0]], [P[1], S[1]], [P[2], S[2]])
ax.plot([R[0], S[0]], [R[1], S[1]], [R[2], S[2]])
ax.plot([Q[0], R[0]], [Q[1], R[1]], [Q[2], R[2]])
ax.text(*P, f'P({P[0]}, {P[1]}, {P[2]})')
ax.text(*Q, f'Q({Q[0]}, {Q[1]}, {Q[2]})')
ax.text(*R, f'R({R[0]}, {R[1]}, {R[2]})')
ax.text(*S, f'S({S[0]}, {S[1]}, {S[2]})')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()
