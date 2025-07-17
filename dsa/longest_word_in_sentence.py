#Wap to find the longest word in a string.

sentence = input("\n Enter the sentence : ")
words = sentence.split()

longest = ""
longest_length = 0

for word in words :
    if len(word) > len(longest) :
        longest = word
        longest_length = len(word)

print("\n Longest word :",longest,"and its length is :",longest_length)
