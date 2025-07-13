a = [1,2,3,4,5]

def reverse_list(lst):
    i = 0  
    j = len(lst) - 1  
    while i < j :
        temp = lst[i] 
        lst[i] = lst[j] # 5
        lst[j] = temp  # 1
        i += 1
        j -= 1
    print("The list is :",lst)

reverse_list(a)

