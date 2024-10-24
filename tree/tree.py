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
            return
        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            if curr.left is None:
                curr.left = Node(val)
                return
            else:
                queue.append(curr.left)
            if curr.right is None:
                curr.right = Node(val)
                return
            else:
                queue.append(curr.right)

    def delete(self, val):
        if not self.root:
            return None
        node_delete = None
        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            if curr.value == val:
                node_delete = curr
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
        if not node_delete:
            return False
        node_delete.value = curr.value
        self._delete_last(curr)

    def _delete_last(self,node):
        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            if curr.left:
                if curr.left == node:
                    curr.left = None
                else:
                    queue.append(curr.left)
            if curr.right:
                if curr.right == node:
                    curr.right = None
                else:
                    queue.append(curr.right)

    def search(self, val):
        if not self.root:
            return False
        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            if curr.value == val:
                return True
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return False

    def find_depth(self, root, key, depth=0):
        if root is None:
            return -1
        if root.value == key:
            return depth
        left_depth = self.find_depth(root.left, key, depth+1)
        if left_depth != -1:
            return left_depth
        return self.find_depth(root.right, key, depth+1)

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left) 
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1

    def inorder(self, node):
        if node is None:
            return None
        self.inorder(node.left)
        print(node.value)
        self.inorder(node.right)



bt = Tree()
bt.insert(10)
# bt.insert(20)
# bt.insert(30)
bt.insert(40)
bt.insert(50)
bt.insert(60)
bt.insert(70)
# bt.insert(80)
bt.inorder(bt.root)
print()
bt.delete(40)
bt.inorder(bt.root)
# print(bt.search(130))
# print(bt.find_depth(bt.root, 40))
# print(bt.height(bt.root))
