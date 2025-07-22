class Node:
    def __init__(self,key):
        self.key = key
        self.right = None
        self.left = None

def insert(root,key):
    if root is None :
        return Node(key)
    if key < root.key :
        root.left = insert(root.left,key)
    else :
        root.right = insert(root.right,key)
    return root

def inorder(root):
    if root :
        inorder(root.left)
        print(root.key,end=' ')
        inorder(root.right)

root = None

values = [50,30,70,20,40,60,80]
for val in values :
    root = insert(root,val)

print("Inorder traversal (sorted) : ")
inorder(root)