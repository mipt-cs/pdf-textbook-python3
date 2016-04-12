5, 3, 8, 6, 9, 1, 2, 7, 4, 10

class node:
    def __init__(self):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


def print_binary_tree(node):
    if not node:
        return
    print(print_binary_tree(node.left))
    print(node.value)
    print(print_binary_tree(node.right)



def tree_search(node, key):
    if not node:
          return NaN
    if node.key == key:
          return node
    if key < node.key:
          return tree_search(node.left, key)
    else:
          return tree.search(node.right, key)
          
          
          
          
    
    
