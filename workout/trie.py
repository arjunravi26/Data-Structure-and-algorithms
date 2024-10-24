class Node:
    def __init__(self) -> None:
        self.child = [None] * 26
        self.wordEnd = False


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, key):
        curr = self.root
        for c in key:
            index = ord(c) - ord('a')
            if curr.child[index] is None:
                curr.child[index] = Node()
            curr = curr.child[index]
        curr.wordEnd = True

    def search(self, key):
        curr = self.root
        for c in key:
            index = ord(c) - ord('a')
            if curr.child[index] is None:
                return False
            curr = curr.child[index]
        return curr.wordEnd

    def delete(self, key):
        def _delete(curr, key, depth=0):
            if curr is None:
                return False
            if depth == len(key):
                if curr.wordEnd:
                    curr.wordEnd = False
                    return not any(curr.child)
                return False
            idx = ord(key[depth]) - ord('a')
            should_del = _delete(curr.child[idx], key, depth+1)
            if should_del:
                curr.child[idx] = None
                return not curr.wordEnd and not any(curr.child)
            return False
        _delete(self.root, key, 0)

    def prefix_search(self, key):
        curr = self.root
        for c in key:
            idx = ord(c) - ord('a')
            if curr.child[idx] is None:
                return False
            curr = curr.child[idx]
            print(chr(idx + ord('a')))
        return True

    def traverse(self, node=None, word=''):
        if node is None:
            node = self.root
        if node.wordEnd:
            print(word)
        for i in range(26):
            if node.child[i] is not None:
                self.traverse(node.child[i], word + chr(ord('a') + i))


trie = Trie()
trie.insert("arjun")
print(trie.search('arjun'))
trie.delete('arjun')
trie.traverse()
trie.prefix_search('ar')
