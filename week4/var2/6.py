def is_exist(list, dict):
    listt = []
    for i in dict:
        for elem in list:
            if elem == dict[i]: 
                listt.append(elem)
    return listt
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason':97}
print(is_exist(roll_number, sample_dict))