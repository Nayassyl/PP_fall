import matplotlib.pyplot as plt
import numpy as np
figure, graph = plt.subplots(2, 2, figsize=(8, 6))
num_points = 150
graph[0][0].set_title("Spring", color="green", weight="bold")
springx = np.random.uniform(low=0, high=8000, size=num_points)
springy = np.random.uniform(low=0, high=0.6, size=num_points)
graph[0][0].scatter(springy, springx, c="green", alpha=0.9, s=10)
graph[0][0].set_xticks(np.arange(0, 0.7, 0.1))
graph[0][0].set_yticks(np.arange(1000, 8001, 1000))

graph[0][1].set_title("Summer", color="yellow", weight="bold")
summerx = np.random.uniform(low=0, high=8000, size=num_points)
summery = np.random.uniform(low=0.15, high=0.8, size=num_points)
graph[0][1].scatter(summery, summerx, c="yellow", alpha=0.9, s=10)
graph[0][1].set_xticks(np.arange(0.3, 0.85, 0.1))
graph[0][1].set_yticks(np.arange(1000, 8001, 1000))

graph[1][0].set_title("Fall or Autumn", color="brown", weight="bold")
fallx = np.random.uniform(low=1000, high=9000, size=num_points)
fally = np.random.uniform(low=0.45, high=0.85, size=num_points)
graph[1][0].scatter(fally, fallx, c="brown", alpha=0.9, s=10)
graph[1][0].set_xticks(np.arange(0.45, 0.86, 0.05))
graph[1][0].set_yticks(np.arange(1000, 9001, 1000))

graph[1][1].set_title("Winter", color="blue", weight="bold")
winterx = np.random.uniform(low=0, high=8500, size=num_points)
wintery = np.random.uniform(low=0.2, high=0.6, size=num_points)
graph[1][1].scatter(wintery, winterx, c="blue", alpha=0.9, s=10)
graph[1][1].set_xticks(np.arange(0.2, 0.7, 0.1))
graph[1][1].set_yticks(np.arange(0,8001,2000))

figure.suptitle("Bike Rentals at Different Temperatures\n By Season",
                color="black", weight="bold")
figure.text(0.5, 0.05, "Normalized Temperature", weight="bold",
            color="black", ha="center", va="center")
figure.text(0.04, 0.4, "Count of Total Rental Bikes",
            rotation=90, weight="bold", color="black")
plt.show()


ax3 = fig.add_subplot(223)
ax3.scatter(day[2][0], day[2][1], c="brown")
ax3.set_title('Fall or Autumn',  color="brown")


ax4 = fig.add_subplot(224)
ax4.scatter(day[3][0], day[3][1], c="blue")
ax4.set_title("Winter",  color="blue")
ax4.set_xlabel("Normalized temperature", position=(-0.1,0))