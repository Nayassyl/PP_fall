def a_b():
    n = int(input())
    while n:
        coordinates = [int(i) for i in input().split()]
        a = (coordinates[1]-coordinates[3])/(coordinates[0] + coordinates[2])
        b = coordinates[1] - coordinates[0] * a
        print(f"({a},{b})")
        n -= 1
a_b()