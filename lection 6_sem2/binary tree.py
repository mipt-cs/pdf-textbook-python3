class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class Tree:
    def __init__(self):
        self.root = None
       
    def print_tree(self):
        def print_subtree(node, prefix):
            if not node:
                return
            if node.right:
                print_subtree(node.right, ' '*len(prefix) + '      ┌')
            print(prefix, (node.key, node.value), sep='')
            if node.left:
                print_subtree(node.left, ' '*len(prefix) + '      └')
        if self.root:
            print_subtree(self.root, '')
        else:
            print('Empty tree!')

    def find_node_by_key(self, key):
        current = self.root
        while current and current.key != key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return current

    def __getitem__(self, key):
        node = self.find_node_by_key()
        return node.value if node else None

    def add_node(self, node):
        if not self.root:
            self.root = node
            return
        current = self.root
        path = [current]
        while current.key != node.key:
            if node.key < current.key:
                if current.left:
                    current = current.left
                    path.append(current)
                else:
                    current.left = node
                    node.parent = current
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = node
                    node.parent = current
                    break
        current.value = node.value

    def add_pair(self, key, value):
        node = Node(key, value)
        self.add_node(node)

    def del_node(self, key):
        node = self.find_node_by_key(key)
        if not node:
            return # no key in tree
        if node.left:
            new_boss_node = node.left
            current = node.left
            while current.right:
                current = current.right
            current.right = node.right
            node.right.parent = current
            new_boss_node.parent = node.parent
        elif node.right:
            new_boss_node = node.right
            new_boss_node.parent = node.parent
        else:
            new_boss_node = None

        if node == self.root:
            self.root = new_boss_node
        else:
            if node == node.parent.left:
                node.parent.left = new_boss_node
            else:  
                node.parent.right = new_boss_node

if __name__ == '__main__':
    '''tree = Tree()
    for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        tree.add_pair(x, ' ')
    tree.print_tree()'''

    tree = Tree()
    for x in [4, 2, 1, 3, 6, 5, 7]:
        tree.add_pair(x, x)
    tree.print_tree()
    tree.add_pair(3, 0)
    tree.print_tree()
    tree.del_node(2)
    tree.print_tree()
