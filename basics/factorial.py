#WAP to find a factorial of a number

#Using for loop :
print('---- Using for Loop :')
num = 5
fact = 1
for i in range(1 , num+1):
    fact = fact * i 

print(f"Factorial of {num} is {fact}.\n")

print("------ Using While loop :")
#Using while loop :
num = 8
fact = 1 
for i in range(1,num +1):
    fact = fact * i

print(f"Factorial of {num} is {fact}.\n")