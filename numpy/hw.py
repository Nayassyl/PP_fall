n1, m1 = [int(i) for i in input("Please enter the dimensions of first matrix:").split()]
n2, m2 = [int(i) for i in input("Please enter the dimensions of second matrix:").split()]

if m1 != n2: 
    print("This matrices cannot be multiplied!")
    n1, m1 = [int(i) for i in input("Please enter the dimensions of first matrix:").split()]
    n2, m2 = [int(i) for i in input("Please enter the dimensions of second matrix:").split()]

arr1 = []
arr2 = []
print("Enter first matrix:")
for i in range(n1):
    row = [int(i) for i in input().split()]
    arr1.append(row)
print("Enter second matrix:")
for i in range(n2):
    row = [int(i) for i in input().split()]
    arr2.append(row)

res = [[sum(arr1[i][k] * arr2[k][j] for k in range(m1)) for j in range(m2)] for i in range(n1)]
print("Resulting array:")
for row in res:
    for elem in row:
        print(elem, end = " ")
    print()