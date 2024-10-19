class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._insert_rec(self.root, val)

    def _insert_rec(self, node, val):
        if val < node.value:
            if node.left is None:
                node.left = Node(val)
                return
            else:
                self._insert_rec(node.left, val)
        elif val > node.value:
            if node.right is None:
                node.right = Node(val)
                return
            else:
                self._insert_rec(node.right, val)

    def delete_node(self, root, key):
        if root is None:
            return root
        if key < root.value:
            root.left = self.delete_node(root.left, key)
        elif key > root.value:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.minvalnode(root.right)
            root.value = temp.value
            root.right = self.delete_node(root.right, temp.value)
        return root

    def search(self, val):
        return self._search_rec(self.root, val)

    def _search_rec(self, node, val):
        if node is None:
            return False
        if val == node.value:
            return True
        elif val < node.value:
            return self._search_rec(node.left, val)
        else:
            return self._search_rec(node.right, val)

    def minvalnode(self, node):
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")

    def preorder(self, node):
        if node is not None:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def sumofnodes(self):
        return self.sum_rc(self.root)

    def sum_rc(self, node):
        if node is None:
            return 0
        return (node.data + self.sum_rc(node.left) + self.sum_rc(node.right))

    def count_rc(self, node):
        if node is None:
            return 0
        return (1+self.count_rc(node.left)+self.count_rc(node.right))

    def countofleaf(self):
        return self.cntofleaf(self.root)

    def cntofleaf(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return (self.cntofleaf(node.left)+self.cntofleaf(node.right))

    def is_bst(self):
        return self.is_bst_rc(self.root, float('-inf'), float('inf'))

    def is_bst_rc(self, node, left, right):
        if node is None:
            return True
        if not (left < node.data < right):
            return False
        return (self.is_bst_rc(node.left, left, node.data)) and (self.is_bst_rc(node.right, node.data, right))

    def findclosest(self, target):
        return self.findclosest_rc(self.root, target)

    def findclosest_rc(self, node, target, closest=None):
        if node is None:
            return closest
        if closest is None:
            closest = node.data
        if abs(target - closest) > abs(target - node.data):
            closest = node.data
        if target < node.data:
            return self.findclosest_rc(node.left, target, closest)
        elif target > node.data:
            return self.findclosest_rc(node.right, target, closest)
        else:
            return closest

    def minvalnode(self, node):
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr


bst = Tree()
bst.insert(10)
bst.insert(20)
bst.insert(30)
bst.insert(40)
bst.insert(50)

print("Preorder traversal:")
bst.preorder(bst.root)
print("\nInorder traversal before deletion:")
bst.inorder(bst.root)

bst.delete_node(bst.root, 40)

print("\nInorder traversal after deleting 40:")
bst.inorder(bst.root)
