stack = []
top = -1
def is_empty(lst):
    if top == -1 :
        return True
    else :
        return False
    
def is_full(lst):
    if top ==(len(lst)-1) :
        return True
    else :
        return False
def peek(lst):
    return peek
while True :
    print("------------Stack-----------")
    print("\n1. Push")
    print("\n2. Pop")
    print("\n3. Is_empty")
    print("\n4. Is_full")
    print("\n5. Peek")
    print("\n6. Exit")

    choice =int(input("\n\nEnter your choice : "))

    if choice == 1 :
        top = top + 1
        data = input("Enter a value to Push : ")
        stack.append(data)
        print(f"{data} pushed into stack\n")
    elif choice == 2 :
        top = top - 1
        stack.pop()
        print("Popped")
    elif choice == 3 :
        print("\nIs stack Empty ?",is_empty(stack))
    elif choice == 4 :
        print("\nIs stack full",is_full(stack))
    elif choice == 5 :
        print("\nPeek :",top)
    elif choice == 6 :
        break
    else :
        print("Invalid choice")