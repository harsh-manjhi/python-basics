numbers = [int(x) for x in input("Enter numbers seperated by spaces : ").split()]
target = int(input("Enter a target : "))
result = []
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] + numbers[j] == target :
            result.append((numbers[i],numbers[j]))
if result :
    print("Pairs that sums",target,":")
    for pair in result :
        print(pair)
else :
    print("No pairs found.")