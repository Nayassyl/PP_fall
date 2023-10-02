def odd_even(list1, list2):
    new_list = []
    for i in range(1, len(list1), 2):
        new_list.append(list1[i])
    for i in range(0, len(list2), 2):
        new_list.append(list2[i])
    return new_list
a = input().split()
b = input().split()
print(odd_even(a, b))