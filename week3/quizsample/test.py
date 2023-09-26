b = [[int(i) for i in input().split()] for j in range(6)]
block = []
for i in range(0, 6, 2):
        for j in range(0, 6, 2):
            block = [row[j:j+2] for row in b[i:i+2]]

        

        