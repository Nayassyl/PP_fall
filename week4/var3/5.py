def is_monotonic(numbers):
    changings = []
    if numbers[0]+1 == numbers[1]:
        is_increasing = 1
    elif numbers[0] == numbers[1]+1:
        is_increasing = 0
    else:
        is_increasing = 2
        changings.append(1)
    for i in range(1, len(numbers)-1):
        if numbers[i]+1 == numbers[i+1]:
            if is_increasing == 0:
                is_increasing = 1
                changings.append(i+1)
        elif numbers[i] == numbers[i+1] + 1:
            if is_increasing == 1:
                is_increasing = 0
                changings.append(i+1)
        else:
            if is_increasing != 2:
                changings.append(i+1)
                is_increasing = 2
    return changings

numbers = [int(i) for i in input().split()]
print(is_monotonic(numbers))