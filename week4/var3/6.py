import math
def area_heron():
    def distance(x1, y1, x2, y2):
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
    n = int(input())
    while n:
        coordinates = [int(i) for i in input().split()]
        a = distance(coordinates[0], coordinates[1],
                     coordinates[2], coordinates[3])
        b = distance(coordinates[0], coordinates[1],
                     coordinates[4], coordinates[5])
        c = distance(coordinates[2], coordinates[3],
                     coordinates[4], coordinates[5])
        polupoker = (a+b+c)/2
        area = math.sqrt(polupoker * (polupoker-a) *
                         (polupoker - b) * (polupoker - c))
        n -= 1
        print(round(area, 1))
area_heron()
