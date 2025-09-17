import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

D1 = np.array([3, 2, 3], dtype=np.float64)
k1 = 16.0
D2 = np.array([3, 2, 3], dtype=np.float64)
k2 = 14.0
D3 = np.array([3, 2, 3], dtype=np.float64)
k3 = 18.0
D4 = np.array([1, 1, 1], dtype=np.float64)
k4 = 7.0

x_vals = np.linspace(-10, 10, 100)
y_vals = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x_vals, y_vals)
Z1 = (k1 - D1[0]*X - D1[1]*Y) / D1[2]
Z2 = (k2 - D2[0]*X - D2[1]*Y) / D2[2]
Z3 = (k3 - D3[0]*X - D3[1]*Y) / D3[2]
Z4 = (k4 - D4[0]*X - D4[1]*Y) / D4[2]

fig = plt.figure(figsize=(12, 10))
ax = plt.axes(projection='3d')

ax.plot_surface(X, Y, Z1, color='magenta', alpha=0.5)
ax.plot_surface(X, Y, Z2, color='green', alpha=0.5)
ax.plot_surface(X, Y, Z3, color='yellow', alpha=0.5)
ax.plot_surface(X, Y, Z4, color='cyan', alpha=0.5)

ax.set_xlim([-20, 20])
ax.set_ylim([-20, 20])
ax.set_zlim([-30, 40])

legend_elements = [
    Patch(facecolor='cyan', alpha=0.7, label='x + y + z = 7'),
    Patch(facecolor='magenta', alpha=0.9, label='3x + 2y + 3z = 16'),
    Patch(facecolor='yellow', alpha=0.9, label='3x + 2y + 3z = 18'),
    Patch(facecolor='green', alpha=0.9, label='3x + 2y + 3z = 14')
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=10)

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.set_title('Plot')
ax.view_init(30,135)
plt.grid()
plt.tight_layout()

plt.savefig("../figs/plot_p.jpg")
plt.show()
