class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.wordEnd = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert_key(self, root, key):
        curr = root
        for c in key:
            index = ord(c) - ord('a')
            if curr.child[index] is None:
                new_node = TrieNode()
                curr.child[index] = new_node
            curr = curr.child[index]
        curr.wordEnd = True

    def search_key(self, root, key):
        curr = root
        for c in key:
            index = ord(c) - ord('a')
            if curr.child[index] is None:
                return False
            curr = curr.child[index]
        return curr.wordEnd

    def prefix_search(self, root, key):
        curr = root
        for c in key:
            index = ord(c) - ord('a')
            if curr.child[index] is None:
                return False
            curr = curr.child[index]
        return True

    def delete_key(self, key):
        def _delete(curr, key, depth):
            if curr is None:
                return False
            if depth == len(key):
                if curr.wordEnd:
                    curr.wordEnd = False
                    return not any(curr.child)
                return False
            index = ord(key[depth]) - ord('a')
            should_delete_current_node = _delete(
                curr.child[index], key, depth + 1)
            if should_delete_current_node:
                curr.child[index] = None
                return not curr.wordEnd and not any(curr.child)
            return False
        return _delete(self.root, key, 0)


trie = Trie()
trie.insert_key(trie.root, 'abc')
trie.insert_key(trie.root, 'hgf')
print(trie.search_key(trie.root, 'hgf'))
print(trie.delete_key("hgf"))
print(trie.search_key(trie.root, 'hgf'))
print(hash("sda"))
