def eggs_mamie(display_value):
    count =0
    while display_value >0:
        if display_value %2 == 1:
            count +=1
        display_value =display_value//2
    return count 
    
    



print(eggs_mamie(16))