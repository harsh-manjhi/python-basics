def search_bst(root,key):
    if not root :
        return None
    if root.val == key :
        return root
    elif key < root.val :
        return search_bst(root.left,key)
    else :
        return search_bst(root.right,key)


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

result = search_bst(root,6)
if result :
    print("Found Value :",result.val)
else :
    print("Not Found")

