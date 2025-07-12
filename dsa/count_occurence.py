a = [6,2,6,4,8,3,4,1,8,0,0,2,4,1]

def check_occurence(lst,num):
    count = 0
    for item in lst :
        if item == num :
            count += 1
    print(f"{num} appears -> {count} times.")

check_occurence(a,6)