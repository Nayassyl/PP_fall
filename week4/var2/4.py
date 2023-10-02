with open("C:\quiz\class_scores.txt") as file:
    for line in file:
        name, score = [i for i in line.split()]
        score = int(score)
        score += 5
        st = name + " " +  str(score)
        with open("C:\quiz\scores2.txt","a") as cringe:
            cringe.write(st+'\n')



        

