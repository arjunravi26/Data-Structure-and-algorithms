class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.right = None
        self.left = None


class Tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.left is None:
                current.left = Node(value)
                return
            else:
                queue.append(current.left)
            if current.right is None:
                current.right = Node(value)
                return
            else:
                queue.append(current.right)

    def search(self):
        pass

    def delete(self, value):
        if not self.root:
            return False
        queue = [self.root]
        node_to_delete = None
        last_node = None
        while queue:
            last_node = queue.pop(0)

            if last_node.value == value:
                node_to_delete = last_node
            if last_node.left:
                queue.append(last_node.left)
            if last_node.right:
                queue.append(last_node.right)
        if not last_node:
            return False
        node_to_delete.value = last_node.value
        self._delete_last(last_node)

    def _delete_last(self, dl_node):
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.left:
                if current.left == dl_node:
                    current.left = None
                else:
                    queue.append(current.left)
            if current.right:
                if current.right == dl_node:
                    current.right = None
                else:
                    queue.append(current.right)

    def search(self, val):
        if not self.root:
            return False
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.value == val:
                return True
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return False

    def inorder(self, node):
        if not node:
            return None
        self.inorder(node.left)
        print(node.value, end=" ")
        self.inorder(node.right)


bt = Tree()
for i in range(10):
    bt.insert(i)
bt.inorder(bt.root)
bt.delete(3)
print()
bt.inorder(bt.root)
print(bt.search(1))
