class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.left = None
        self.right = None


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return
        self._insert_recur(self.root, val)

    def _insert_recur(self, node, val):
        if val < node.value:
            if node.left is None:
                node.left = Node(val)
            else:
                self._insert_recur(node.left, val)
        elif val > node.value:
            if node.right is None:
                node.right = Node(val)
            else:
                self._insert_recur(node.right, val)
        else:
            return

    def delete(self, key, node):
        if self.root is None:
            return None
        while node:
            if key < node.value:
                node.left = self.delete(key, node.left)
            elif key > node.value:
                node.right = self.delete(key, node.right)
            else:
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                temp = self.find_min(node.right)
                node.value = temp.value
                node.right = self.delete(temp.value, node.right)
            return node

    def search(self, key):
        def _search(node, key):
            if node is None:
                return False
            if node.value == key:
                return True
            elif key < node.value:
                return _search(node.left, key)
            else:
                return _search(node.right, key)
        if self.root is None:
            return False
        return _search(self.root, key)

    def sum_of_nodes(self):
        return self._sum_nodes_rc(self.root)

    def _sum_nodes_rc(self, node):
        if node is None:
            return 0
        return (node.value + self._sum_nodes_rc(node.left) + self._sum_nodes_rc(node.right))

    def findclosetnode(self, target):
        return self.findcloset_rc(self.root, target)

    def findcloset_rc(self, node, target, closet=None):
        if node is None:
            return closet
        if closet is None:
            closet = node.value
        if abs(node.value - target) < abs(node.value - closet):
            closet = node.value
        if target < node.value:
            self.findcloset_rc(node.left, target, closet)
        else:
            self.findcloset_rc(node.right, target, closet)
        return closet

    def find_min(self, node):
        if node is None:
            return None
        current = node
        while current.left:
            current = current.left
        return current

    def postorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        self.inorder(node.right)
        print(node.value)

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.value)
        self.inorder(node.right)

    def preorder(self, node):
        if node is None:
            return
        print(node.value)
        self.inorder(node.left)
        self.inorder(node.right)

    def height(self, node):
        if node is None:
            return -1
        left = self.height(node.left)
        right = self.height(node.right)
        return max(left, right) + 1
    def depth(self,root,key,depth=0):
        if root is None:
            return -1
        if root.value == key:
            return depth
        left = self.depth(root.left,key,depth+1)
        if left != -1:
            return depth
        return self.depth(root.right,key,depth+1)


tree = BST()
tree.insert(10)
tree.insert(20)
tree.insert(0)
tree.insert(100)
# tree.delete(10, tree.root)
tree.inorder(tree.root)
print(tree.search(20))
print(tree.sum_of_nodes())
print(tree.findclosetnode(20))
print(tree.depth(tree.root,100))
print(tree.height(tree.root))
