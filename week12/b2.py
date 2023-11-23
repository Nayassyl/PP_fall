import matplotlib.pyplot as plt
figure, graph = plt.subplots()
plt.xlabel('x')
plt.ylabel('y')

plt.axvline(x=5, color="#00FF00")
graph.text(5, 4, "0,000", color="#00FF00", verticalalignment="bottom",
           horizontalalignment="center", rotation=90)

graph.set_xlim(0, 10)
graph.set_ylim(0, 8)

circle1 = plt.Circle((2.1, 4), 1.8, fill=False, color="#AA8800")
graph.add_patch(circle1)
graph.set_aspect("equal")
graph.text(2, 2, "0.250", color='#AA8800', verticalalignment='bottom',
           horizontalalignment='center', rotation=-6)
circle_2 = plt.Circle((2.1, 4), 1.3, fill=False, color='red')
graph.add_patch(circle_2)
graph.set_aspect('equal')
graph.text(2.9, 4.5, '0.500', color='red', verticalalignment='bottom',
        horizontalalignment='center', rotation=-45)

circle_3 = plt.Circle((2.1, 4), 0.8, fill=False, color='brown')
graph.add_patch(circle_3)
graph.set_aspect('equal')
graph.text(2, 4.6, '0.750', color='brown', verticalalignment='bottom',
        horizontalalignment='center', rotation=0)

circle_4 = plt.Circle((7.9, 4), 1.8, fill=False, color='#00BBFF')
graph.add_patch(circle_4)
graph.set_aspect('equal')
graph.text(6, 3.7, '-0.250', color='#00BBFF', verticalalignment='bottom',
        horizontalalignment='center', rotation=-90)

circle_5 = plt.Circle((7.9, 4), 1.3, fill=False, color='#0000FF')
graph.add_patch(circle_5)
graph.set_aspect('equal')
graph.text(8, 5, '-0.500', color='#0000FF', verticalalignment='bottom',
        horizontalalignment='center', rotation=-10)

circle_6 = plt.Circle((7.9, 4), 0.8, fill=False, color='#FF77FF')
graph.add_patch(circle_6)
graph.set_aspect('equal')
graph.text(8, 4.5, '-0.750', color='#FF77FF', verticalalignment='bottom',
        horizontalalignment='center', rotation=-10)
plt.show()