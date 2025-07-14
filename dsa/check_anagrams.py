# Wap to check if two strings are anagrams
def is_anagrams(s1,s2):
    print("String 1 :",s1)
    print("String 2 :",s2)
    if len(s1) != len(s2):
        return print("Not anagrams.")
    # Sorting the First string
    first = sorted(s1)
    # Sorting the First string
    second = sorted(s2)
    # Checking if they are anagrams
    if first == second :
        print("Strings are anagrams.")
    else :
        print("Not anagrams.")


is_anagrams('abcd','bcda')
