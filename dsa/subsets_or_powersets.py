def subsets(nums):
    result = []
    
    n = len(nums)
    def backtrack(start,path):
        result.append(path[:])

        for i in range(start,n):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0,[])
    return result
    
print(subsets([1,2]))