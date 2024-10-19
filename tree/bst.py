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
        elif val > node.value:  # Skipping duplicates
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
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children, get the inorder successor
            temp = self.minvalnode(root.right)
            root.value = temp.value  # Fixed the attribute to 'value'
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
            return self._search_rec(node.left, val)  # Fixed incorrect function call
        else:
            return self._search_rec(node.right, val)

    def minvalnode(self, node):
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr

    # Traversal methods:
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
            self.preorder(node.left)  # Fixed traversal method call
            self.preorder(node.right)  # Fixed traversal method call

# Example usage
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
