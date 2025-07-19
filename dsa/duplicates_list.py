lists = [1,2,5,2,1,3,5,1]

def find_duplicates(nums):
    seen = set()
    duplicate = set()
    for num in nums :
        if num in seen :
            duplicate.add(num)
        else :
            seen.add(num)
        
    return list(duplicate)

print(find_duplicates(lists))