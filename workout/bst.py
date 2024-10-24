class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert_rc(self.root, val)

    def _insert_rc(self, node, val):
        if val < node.data:
            if node.left is None:
                node.left = Node(val)
                return
            else:
                self._insert_rc(node.left, val)
        elif val > node.data:
            if node.right is None:
                node.right = Node(val)
                return
            else:
                self._insert_rc(node.right, val)
        else:
            return

    def search(self, key):
        def _search(node, key):
            if node is None:
                return False
            if node.data == key:
                return True
            elif key < node.data:
                return _search(node.left, key)
            else:
                return _search(node.right, key)

        return _search(self.root, key)

    def delete(self, key):
        def _delete(node, key):
            if key < node.data:
                node.left = _delete(node.left, key)
            elif key > node.data:
                node.right = _delete(node.right, key)
            else:
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                temp = self.find_min_node(node.right)
                node.data = temp.data
                node.right = _delete(node.right, temp.data)
            return node
        return _delete(self.root, key)

    def find_min_node(self, node):
        if node is None:
            return None
        curr = node
        while curr.left:
            curr = curr.left
        return curr

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)

    def sum_node(self):
        return self._sumrc(self.root)

    def _sumrc(self, node):
        if node is None:
            return 0
        return (node.data + self._sumrc(node.left) + self._sumrc(node.right))

    def sum_leaves(self):
        return self._sumleaves_rc(self.root)

    def _sumleaves_rc(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return node.data
        else:
            return self._sumleaves_rc(node.left) + self._sumleaves_rc(node.right)
    def height(self,node):
        if node is None:
            return 0
        left = self.height(node.left)
        right = self.height(node.right)
        return max(left,right) + 1
    def depth(self,node,key,depth = 0):
        if node is None:
            return -1
        if node.data == key:
            return depth
        left = self.depth(node.left,key,depth+1)
        if left != -1:
            return depth
        return self.depth(node.right,key,depth+1)
        


bst = BST()
bst.insert(10)
bst.insert(20)
bst.insert(15)
bst.insert(18)
bst.insert(0)
bst.insert(50)
bst.insert(30)
bst.inorder(bst.root)
print(bst.search(100))
bst.delete(10)
bst.inorder(bst.root)
print(bst.sum_node())
print(bst.sum_leaves())
print(bst.height(bst.root))
print(bst.depth(bst.root,10))
