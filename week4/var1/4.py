def question4():
    with open("students.txt", 'r') as file:
        with open("students2.txt", 'w') as new_file:
            for i in file:
                elements = i.split(' ')
                elements[0] = elements[0].capitalize()
                elements[1] = elements[1].capitalize()
                elements[len(elements) - 1] = '301-' + elements[len(elements) - 1]
                for j in elements:
                    new_file.write(j+' ')
                new_file.write('\n')