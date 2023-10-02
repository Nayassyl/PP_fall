def sequence(numbers):
    for i in numbers:
        count = 0
        while i != 1:
            if i & 1:
                i = i * 3 + 1
            else:
                i //= 2
            count += 1
        print(count, end=' ')

numbers = [int(i) for i in input().split()]
sequence(numbers)


    