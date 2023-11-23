import matplotlib.pyplot  as plt
import numpy as np 
x = np.array(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
y = np.array([25,47,75,8,17,66,29])
colors = ["red", "blue", "orange", "green", "pink", "yellow", "purple"]
plt.bar(x,y, color = colors)
plt.title("Weekday data")
plt.show()