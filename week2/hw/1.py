s = "";    
for i in range(0,7):    
    for j in range(0,7):     
        if (((j == 1 or j == 5) and i != 0 and i != 6) or ((i == 0 or i == 6) and j > 1 and j < 5)):  
            s += "*"    
        else:      
            s += " "    
    s += "\n"    
print(s);    