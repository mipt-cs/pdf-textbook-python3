class Tree:
    class Node:
        def __init__(self, data):
            self.parent = None
            self.left = None
            self.right = None
            self.key = data
    def __init__(self):
        self.root = None
    def find(self, data):
        p = self.root
        while p is not None and p.key != data:
            if data > p.key:
                p = p.right
            else:
                p = p.left
        return p
    def insert(self, data):
        p = self.find(data)
        if p is not None:
            return
        node = Tree.Node(data)
        if self.root is None:
            self.root = node
            return
        p = self.root
        while True:
            if data < p.key:
                if p.left is None:
                    p.left = node
                    node.parent = p
                    break
                else:
                    p = p.left
            else:
                if p.right is None:
                    p.right = node
                    node.parent = p
                    break
                else:
                    p = p.right