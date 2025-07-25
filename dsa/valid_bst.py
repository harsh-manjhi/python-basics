class Node :
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def is_valid_bst(root):
    def helper(node,low,high):
        if not node :
            return True
        
        if not (low < node.val < high) :
            return False
        
        return helper( node.left, low, node.val ) and helper( node.right, node.val, high)
    
    return helper(root, float('-inf'), float('inf'))


# Sample 1 
root1 = Node(8)
root1.left = Node(3)
root1.right = Node(10)
root1.left.left = Node(1)
root1.left.right = Node(6)
root1.right.right = Node(14)

print("Is root1 a Valid BST ? :", is_valid_bst(root1))

root2 = Node(10)
root2.left = Node(5)
root2.right = Node(15)
root2.right.left = Node(6)  

print("\nIs root2 a valid BST?  :", is_valid_bst(root2))  