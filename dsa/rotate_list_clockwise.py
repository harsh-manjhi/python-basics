#    -5-4-3-2-1
example_array =[1,2,3,4,5,6]
#     0 1 2 3 4
print("Array before :",example_array)
def rotateClockwise(arr,k):

    n = len(arr)    
    k = k % n

    # Reversing last k elements
    arr[n - k : ] = reversed(arr[n - k : ])

    # Reverse n - k elements
    arr[: n - k] = reversed(arr[: n - k])

    # Reverse whole array
    arr[ : ] = reversed(arr[ : ])

rotateClockwise(example_array,1)
print("Array after rotations :",example_array)
