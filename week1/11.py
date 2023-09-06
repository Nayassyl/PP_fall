def distance(x1,y1,x2,y2):
    print(((x2-x1)**2 + (y2-y1)**2)**0.5)

x1, y1 = [int(i) for i in input("coordinates of first dot:").split()]
x2, y2 = [int(i) for i in input("coordinates of second dot:").split()]
distance(x1, y1, x2, y2)