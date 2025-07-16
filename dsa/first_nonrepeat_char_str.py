string = input("Enter a string : ")
char_counts ={}
# Counting characters
for char in string :
    if char in char_counts :
        char_counts[char] += 1
    else :
        char_counts[char] = 1

for char in string :
    if char_counts[char] == 1:
        print("First non-repeating word : ",char)
        found = True
        break
if not found :
        print("No non-repeating word found")