
char_counts = {}

def char_frequency(s):
    for char in s :
        if char in char_counts :
            char_counts[char] += 1
        else :
            char_counts[char] = 1 

    display_counts()


def display_counts() :
    for char,count in char_counts.items() :
        print(f"\n {char} : {count}")

print("\n ----To check the frequency of Each character----")
string = input("\n Enter a string : ")

char_frequency(string)