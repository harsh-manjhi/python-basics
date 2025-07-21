class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def insert(self,data):
        new_node = Node(data)
        if self.head is None :
            self.head = new_node
            return
        current = self.head
        while current.next :
            current = current.next
        current.next = new_node

    def print_list(self) :
        current = self.head
        while current :
            print(current.data,end = "->")
            current = current.next
        print("None")


llist = Linkedlist()
llist.insert(10)
llist.insert(20)
llist.insert(30)

llist.print_list()