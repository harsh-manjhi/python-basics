def second_largest(lst):
    first = second = float('-inf')
    for num in lst :
        if num > first :
            second = first
            first = num 
        elif num > second and num < first :
            second = num

    if second == float('-inf'):
        print("No second largest number found.")
    else:
        print("Second largest number :",second)

a = [1,2,8,3,8,0]

second_largest(a)