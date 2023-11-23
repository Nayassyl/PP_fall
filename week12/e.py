import matplotlib.pyplot as plt
import numpy as np
num_points = 60
x = np.random.uniform(low=-0.2, high=1.2, size=num_points)
y = np.random.uniform(low=-0.2, high=1.2, size=num_points)
colors = np.random.randint(100, size=(num_points))
sizes = 10 * np.random.randint(100, size=(num_points))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.4, cmap='nipy_spectral')

# plt.colorbar()

plt.show()