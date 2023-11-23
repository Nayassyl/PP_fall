import matplotlib.pyplot as plt
r1 = 7
r2 = 5
r3 = 2
figure, graph = plt.subplots()
circle1 = plt.Circle((0, 0), r1, fill=False)
circle2 = plt.Circle((0, -2), r2, fill=False)
circle3 = plt.Circle((0, -5), r3, fill=False)
graph.add_patch(circle1)
graph.add_patch(circle2)
graph.add_patch(circle3)
graph.set_xlim(-10,10)
graph.set_ylim(-10,10)
plt.text(7,0,'-----100')
plt.text(5,-2.5,'---------50')
plt.text(2,-5,'--------------------10')
graph.set_axis_off()
plt.show()
