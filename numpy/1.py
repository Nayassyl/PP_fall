import numpy

def t1():
    arr = numpy.empty([4,2], dtype = numpy.uint16) 
    print("Printing Array")
    print(arr)

    print("Printing np array Attributes")
    print("1> Array Shape is: ", arr.shape)
    print("2>. Array dimensions are ", arr.ndim)
    print("3>. Length of each element of array in bytes is ", arr.itemsize)

def t2():
    print("Creating 5X2 array using numpy.arange")
    arr = numpy.arange(100, 200, 10)
    arr = arr.reshape(5,2)
    print (arr)

def t3():
    arr = numpy.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]]) 
    print("Printing Input Array")
    print(arr)

    print("Printing array of items in the third column from all rows")
    arr2 = arr[...,2]
    print(arr2)
def t4():
    arr = numpy.array([[3 ,6, 9, 12], [15 ,18, 21, 24], [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]]) 
    print("Printing Input Array")
    print(arr)
    print("\n Printing array of odd rows and even columns")
    arr2 = arr[::2, 1::2]
    print(arr2)

def t5():
    arr1 = numpy.array([[5, 6, 9], [21 ,18, 27]])
    arr2 = numpy.array([[15 ,33, 24], [4 ,7, 1]])

    arr  = arr1 + arr2
    print("addition of two arrays is \n")
    print(arr)

    for num in numpy.nditer(arr, op_flags = ['readwrite']):
        num[...] = num * num
    print("\nResult array after calculating the square root of all elements\n")
    print(arr)

def t6():
    print("Creating 8X3 array using numpy.arange")
    arr = numpy.arange(10, 34, 1)
    arr = arr.reshape(8,3)
    print (arr)

    print("\nDividing 8X3 array into 4 sub array\n")
    sarr = numpy.split(arr, 4) 
    print(sarr)


def t7():
    sampleArray = numpy.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

    bycolumn = sorted(sampleArray, key=lambda x: x[1])
    print(numpy.array(bycolumn))



    tobyrow = numpy.transpose(sampleArray)
    byrow = sorted(tobyrow, key = lambda x: x[1])

    print(numpy.array(numpy.transpose(byrow)))


def t8():
    arr = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
    print("Printing Original Array")
    print(arr)
    import numpy

    min1 = numpy.amin(arr, 1) 
    print("Printing amin Of Axis 1")
    print(min1)

    max0 = numpy.amax(arr, 0) 
    print("Printing amax Of Axis 0")
    print(max0)

def t9():
    print("Printing Original array")
    arr = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
    print (arr)

    print("Array after deleting column 2 on axis 1")
    arr = numpy.delete(arr , 1, axis = 1) 
    print (arr)

    arr2 = numpy.array([[10,10,10]])
    print("Array after inserting column 2 on axis 1")
    arr = numpy.insert(arr , 1, arr2, axis = 1) 
    print (arr)
