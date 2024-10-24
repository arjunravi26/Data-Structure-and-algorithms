class Node:
    def __init__(self, val) -> None:
        self.data = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return
        self._insert_rc(self.root, val)

    def _insert_rc(self, node, val):
        if val < node.data:
            if node.left is None:
                node.left = Node(val)
                return
            self._insert_rc(node.left, val)
        elif val > node.data:
            if node.right is None:
                node.right = Node(val)
                return
            self._insert_rc(node.right, val)
        else:
            return
    def inorder(self):
        def _inorder(node):
            if node is None:
                return
            _inorder(node.left)
            print(node.data)
            _inorder(node.right)
        _inorder(self.root)

tree = Tree()
tree.insert(10)
tree.insert(20)
tree.insert(0)
tree.insert(50)
tree.inorder()