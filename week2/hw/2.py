s = "";    
for i in range(0,7):    
    for j in range(0,7):     
        if (j == 1 or ((i == 0 or i == 3) and j > 1 and j < 5) or (j == 5 and i != 0 and i < 3) or (j == i - 1 and i > 3)):  
            s += "*"    
        else:      
            s += " "    
    s += "\n"    
print(s);        