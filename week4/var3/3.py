def two_to_three():
    with open("file1.txt", 'r') as file1:
        with open("file2.txt", 'r') as file2:
            with open("file3.txt", 'w') as file3:
                lines1 = []
                lines2 = []
                for i in file1:
                    if i[len(i)-1] == '\n':
                        lines1.append(i[:len(i)-1])
                    else:
                        lines1.append(i)
                for i in file2:
                    if i[len(i)-1] == '\n':
                        lines2.append(i[:len(i)-1])
                    else:
                        lines2.append(i[:len(i)-1])
                for i in range(min(len(lines1), len(lines2))):
                    file3.write(lines1[i] + ' ' + lines2[i] + '\n')