def missing_number(arr):
    n = len(arr) + 1
    expected_sum = n*(n+1)//2
    actual_sum = sum(arr)
    result = expected_sum - actual_sum
    return result

example_array = [1,2,3,5]
test = missing_number(example_array)
print("Missing number :",test)