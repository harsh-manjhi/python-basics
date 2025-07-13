a = [1,3,4,2,6,1,2,3,3,4,4,5]
def remove_duplicate(lst):
    result = []
    for item in lst :
        if item not in result :
            result.append(item)
    print("Duplicate removed :",result)

remove_duplicate(a)
