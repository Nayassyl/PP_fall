from sympy import *
import matplotlib.pyplot as plt
import numpy as np
x, y = symbols('x y')
func = x ** 2 
x_values = np.arange(-1, 1.001, 0.001)
y_values = [func.subs({x: point}).evalf() for point in x_values]
plt.plot(x_values, y_values, color = "blue")
plt.show()

