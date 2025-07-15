#Wap to find the longest word in a string.

sentence = input("Enter the sentence : ")
words = sentence.split()
longest = ""
for word in words :
    if len(word) > len(longest) :
        longest = word
print("Longest word :",longest)