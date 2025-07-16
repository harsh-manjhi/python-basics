queue = []

def enqueue():
    value = input("\nEnter value to insert : ")
    queue.append(value)
    print("\nEnqueued",value,".")

def dequeue() :
    if is_empty() :
        print("\nFailed! Queue is Empty")
    else :
        queue.pop(0)
        print(f"\nQueue dequeued ",queue)

def peek():
    if is_empty() :
        print("\nFailed! queue is empty, cannot peek")
        return None
    else :
        return queue[0]

def is_empty():
    if len(queue) == 0 :
        return True
    else :
        return False
    
def display() :
    print("\n'Queue' : ",queue)
    
print("\n\n------------Queue-----------")
    
while True :
    print("\n1. Enqueue")
    print("\n2. Dequeue")
    print("\n3. Peek")
    print("\n4. Is_empty")
    print("\n5. Display")
    print("\n6. Exit")

    choice = int(input("\n\nEnter your choice : "))

    if choice == 1 :
        enqueue()
    elif choice == 2 :
        dequeue()
    elif choice == 3 :
        print("Peek : ",peek())
    elif choice == 4 :
        print("Is queue empty? ",is_empty())
    elif choice == 5 :
        display()
    elif choice == 6 :
        break
    else :
        print("Invalid! choice")