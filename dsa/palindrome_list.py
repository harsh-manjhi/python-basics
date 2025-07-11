a = [1,3,5,6,5,3,1]
def check_palindrome(lst):
    i = 0
    j = len(lst) - 1 
    while i < j :
        if lst[i] != lst[j] :
            return False
        i += 1
        j -= 1
        return print("The Given list is Palindrome.")
    
check_palindrome(a)