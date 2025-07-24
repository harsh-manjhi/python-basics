def find_min(node): # Helper function
    while node.left :
        node = node.left
    return node

def delete_node(root,key):
    if not root :
        return None
    
    # Step 1 Search for key 

    if key < root.val :
        root.left = delete_node(root.left,key)
    elif key > root.val :
        root.right = delete_node(root.right,key)
    else :      # Node to delete 

        # Case 1 : No children (Leaf)
        if not root.left and not root.right :
            return None
        
        # Case 2 : Only one children node 
        elif not root.left :
            return root.right
        elif not root.right :
            return root.left
        
        # Case 3 : Two children
        successor = find_min(root.right)
        root.val = successor.val
        root.right = delete_node(root.right,successor.val)

    return root

class Node :
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)

def inorder(root):  # Helper function
    if not root :
        return None
    else :
        inorder(root.left)
        print(root.val,end = ' ')
        inorder(root.right)

print("Before deletion :")
inorder(root)

root = delete_node(root,3)

print("\n After deletion :")
inorder(root)