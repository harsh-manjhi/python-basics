def is_balanced_tree(root):
    def check_balance(root):
        if not root :
            return True, 0
            #is_curr_balanced,height 
        
        # Check left + right subtree

        left_balanced, left_height = check_balance(root.left)
        right_balanced, right_height = check_balance(root.right)

        is_curr_balanced = (
            left_balanced and right_balanced and abs(left_height - right_height) <= 1   
        )
        
        height = 1 + max(left_height,right_height)

        return is_curr_balanced, height
    balanced, _ = check_balance(root)
    return balanced

class Node :
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

# Sample tree

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)

if is_balanced_tree(root) :
    print("Tree is Balanced.")
else :
    print("Tree is Not balanced.")