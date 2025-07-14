# Wap to remove duplicates from the List
a = [1,3,4,2,6,1,2,3,3,4,4,5]   # sample list
def remove_duplicate(lst):  
    result = []                 # Temp list
    for item in lst :
        if item not in result :
            result.append(item)
    print("Duplicate removed :",result)

remove_duplicate(a)
